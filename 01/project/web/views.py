from django.shortcuts import render, redirect
from .models import Review
from .forms import ReviewForm

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
