from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from .models import Review, ReviewDetail


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'is_staff']


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = [
            'id',
            'name',
            'review',
            'rating',
        ]


class ReviewDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = ReviewDetail
        fields = [
            'id',
            'detail',
        ]