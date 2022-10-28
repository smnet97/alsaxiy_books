from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

from .models import BookModel, CategoryModel
from .serializers import BookModelSerializer, BookModelDetailSerializer, CategoryModelSerializer
from rest_framework.permissions import AllowAny


class CategoryBooksAPIView(APIView):

    def get(self, request, pk, **kwargs):
        qs = BookModel.objects.filter(category=pk)
        serializer = BookModelSerializer(qs, many=True)
        return Response({
            'books': serializer.data
        })


class BookDetailAPIView(RetrieveAPIView):
    permission_classes = [AllowAny, ]
    serializer_class = BookModelDetailSerializer
    queryset = BookModel.objects.all()


class BookModelListAPIView(ListAPIView):
    permission_classes = [AllowAny, ]
    filter_backends = [filters.SearchFilter, ]
    search_fields = ['title', ]

    def list(self, request, *args, **kwargs):
        queryset = BookModel.objects.all()
        serializer = BookModelSerializer(queryset, many=True)
        cat_qs = CategoryModel.objects.all()
        cat_serializer = CategoryModelSerializer(cat_qs, many=True)
        return Response({
            'books': serializer.data,
            'categories': cat_serializer.data,
        })
