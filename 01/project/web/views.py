from django.shortcuts import render
from .models import Review


def reviewView(request):
    items = Review.objects.all()
    return render(request, 'reviews/index.html', {
        "items": items,
    })