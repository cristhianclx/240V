from django.http import Http404
from django.shortcuts import render, redirect
from .models import Review, ReviewDetail
from .forms import ReviewForm, ReviewDetailForm

def reviewView(request):
    items = Review.objects.all()
    return render(request, 'reviews/index.html', {
        "items": items,
    })

def reviewAddView(request):
    success = False
    if request.method == "GET":
        form = ReviewForm()
        return render(request, 'reviews/add.html', {
            "form": form,
        })
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            success = True
        return render(request, 'reviews/add.html', {
            "form": form,
            "success": success,
        })

def reviewDetailView(request, index):
    item = Review.objects.get(id = index)
    return render(request, 'reviews/detail.html', {
        "item": item,
    })

def reviewDeleteView(request, index):
    item = Review.objects.get(id = index)
    if request.method == "GET":
        return render(request, 'reviews/delete.html', {
           "item": item,
        })
    if request.method == "POST":
        item.delete()
        return redirect("/reviews/")

def reviewUpdateView(request, index):
    item = Review.objects.get(id = index)
    success = False
    if request.method == "GET":
        form = ReviewForm(instance = item)
        return render(request, 'reviews/update.html', {
            "form": form,
            "item": item,
        })
    if request.method == "POST":
        form = ReviewForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            success = True
        return render(request, 'reviews/update.html', {
            "form": form,
            "item": item,
            "success": success,
        })

def reviewDetailsListView(request, index):
    try:
        item = Review.objects.get(id = index)
    except Review.DoesNotExist:
        raise Http404
    items = ReviewDetail.objects.filter(review = item).all()
    return render(request, 'review-details/index.html', {
        "items": items,
        "item": item,
    })

def reviewDetailsAddView(request, index):
    try:
        item = Review.objects.get(id = index)
    except Review.DoesNotExist:
        raise Http404
    success = False
    if request.method == "GET":
        form = ReviewDetailForm()
        return render(request, 'review-details/add.html', {
            "form": form,
            "item": item,
        })
    if request.method == "POST":
        form = ReviewDetailForm(request.POST)
        if form.is_valid():
            review_detail = form.save(commit=False)
            review_detail.review = item
            review_detail.save()
            success = True
        return render(request, 'review-details/add.html', {
            "form": form,
            "item": item,
            "success": success,
        })