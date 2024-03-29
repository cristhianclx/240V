from rest_framework import routers, serializers, viewsets, status, permissions
from django.http import JsonResponse
from django.views.generic import View
from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.response import Response
from .serializers import UserSerializer, ReviewSerializer, ReviewDetailSerializer, EditionSerializer
from .models import Review, ReviewDetail, Edition
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie, vary_on_headers

class PingView(View):
    def get(self, request):
        context = {
            "message": "pong - v1",
        }
        return JsonResponse(context)


class UserView(viewsets.ModelViewSet): # CRUD
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ReviewView(viewsets.ModelViewSet): # CRUD
    permission_classes = [permissions.IsAuthenticated]
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    filterset_fields = ['rating',]
    search_fields = ['name', 'review',]


class ReviewDetailView(viewsets.ModelViewSet): # CRUD
    serializer_class = ReviewDetailSerializer

    def get_queryset(self):
        review_id = self.kwargs['review_id']
        return ReviewDetail.objects.filter(review__id = review_id).all()

    def create(self, request, *args, **kwargs):
        review_id = self.kwargs['review_id']
        review_parent = Review.objects.get(id = review_id)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer, review_parent)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def perform_create(self, serializer, review_parent):
        serializer.save(review=review_parent)


#class EditionView(viewsets.ReadOnlyModelViewSet):
#    queryset = Edition.objects.select_related('book', 'book__author',).all()
#    serializer_class = EditionSerializer


class EditionView(viewsets.ViewSet):
    queryset = Edition.objects.select_related('book', 'book__author',).all()
    serializer_class = EditionSerializer

    @method_decorator(cache_page(60 * 60 * 24))
    @method_decorator(vary_on_cookie)
    def list(self, request, format=None):
        queryset = Edition.objects.select_related('book', 'book__author',).all()
        content = self.serializer_class(queryset, many=True)
        return Response(content.data)