from django.http import Http404
from django.shortcuts import render, redirect
from django.views.generic import View

import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

from .models import Document, DocumentMatch
from .forms import DocumentForm
from .utils import parseFileInformation, wrangler, job_vectorizer, job_matrix, ranker, allow_only_peruvian_people


class IndexView(View):

    def get(self, request):
        form = DocumentForm()
        return render(
            request,
            "index.html",
            {
                "form": form,
            },
        )

    def post(self, request):
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save()
            parsed_information_raw = parseFileInformation(instance.document)
            if instance.motivation_document:
                parsed_information_raw = parsed_information_raw + parseFileInformation(instance.motivation_document)
            if not allow_only_peruvian_people(parsed_information_raw):
                return redirect("index")
            parsed_information = wrangler(parsed_information_raw)
            cv_serie = pd.Series(parsed_information)
            cv_matrix = job_vectorizer.transform(cv_serie)
            ranking = cosine_similarity(cv_matrix, job_matrix, True)
            ranking_serie = pd.Series(ranking[0])
            ranker["RANKING"] = ranking_serie
            ranker_final = ranker.sort_values("RANKING", ascending=False)
            match_to_save = []
            for rank_ind in ranker_final.index:
                if ranker_final["RANKING"][rank_ind] >= 0.15:
                    match_to_save.append(
                        DocumentMatch(
                            position=ranker_final["PUESTO"][rank_ind],
                            ranking=ranker_final["RANKING"][rank_ind] * 100,
                            document=instance,
                        )
                    )
            if len(match_to_save) > 0:
                DocumentMatch.objects.bulk_create(match_to_save)
            return redirect("results", id=instance.id)
        return redirect("index")


class ResultsView(View):

    def get(self, request, id):
        try:
            instance = Document.objects.get(id=id)
        except Document.DoesNotExist:
            raise Http404
        matches = (
            DocumentMatch.objects.filter(
                document=instance,
            )
            .all()
            .order_by("-ranking")
        )
        return render(
            request,
            "results.html",
            {
                "instance": instance,
                "matches": matches,
            },
        )
