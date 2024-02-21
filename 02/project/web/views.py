from rest_framework import routers, serializers, viewsets
from django.shortcuts import render
from django.contrib.auth.models import User
from .serializers import UserSerializer


class UserView(viewsets.ModelViewSet): # CRUD
    queryset = User.objects.all()
    serializer_class = UserSerializer