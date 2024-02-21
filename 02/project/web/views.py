from rest_framework import routers, serializers, viewsets
from django.shortcuts import render
from django.contrib.auth.models import User
from .serializers import UserSerializer, ReviewSerializer
from .models import Review


class UserView(viewsets.ModelViewSet): # CRUD
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ReviewView(viewsets.ModelViewSet): # CRUD
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    filterset_fields = ['rating',]
    search_fields = ['name', 'review',]