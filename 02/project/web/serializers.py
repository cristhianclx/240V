from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from .models import Review, ReviewDetail, Edition, Book, Author


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


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = [
            "id",
            "name",
        ]


class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(
        read_only=True,
    )
    class Meta:
        model = Book
        fields = [
            "id",
            "author",
            "name",
        ]


class EditionSerializer(serializers.ModelSerializer):
    book = BookSerializer(
        read_only=True,
    )
    class Meta:
        model = Edition
        fields = [
            "id",
            "book",
            "name",
        ]
