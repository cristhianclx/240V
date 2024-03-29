"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from web.views import reviewView, reviewAddView, reviewDetailView, reviewDeleteView, reviewUpdateView, reviewDetailsListView, reviewDetailsAddView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('reviews/', reviewView, name="reviews-index"),
    path('reviews/add/', reviewAddView, name="reviews-add"),
    path('reviews/<index>/', reviewDetailView, name="reviews-detail"),
    path('reviews/<index>/delete/', reviewDeleteView, name="reviews-delete"),
    path('reviews/<index>/update/', reviewUpdateView, name="reviews-update"),
    path('reviews/<index>/details/', reviewDetailsListView, name="reviews-details"),
    path('reviews/<index>/details/add/', reviewDetailsAddView, name="reviews-details-add"),
]

