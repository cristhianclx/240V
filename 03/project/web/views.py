from django.http import Http404
from django.shortcuts import render, redirect
from django.views.generic import View

from .models import Document
from .forms import DocumentForm


class IndexView(View):

    def get(self, request):
        form = DocumentForm()
        return render(request, "index.html", {
            "form": form,
        })
    
    def post(self, request):
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save()
            # TO-DO
            return redirect('results', id=instance.id)
        return redirect('index')


class ResultsView(View):

    def get(self, request, id):
        try:
            instance = Document.objects.get(id = id)
        except Document.DoesNotExist:
            raise Http404
        return render(request, "results.html", {
            "instance": instance,
        })