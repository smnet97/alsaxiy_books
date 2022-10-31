from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

from .models import BookModel, CategoryModel
from .paginations import BooksPagination
from .serializers import BookModelSerializer, BookModelDetailSerializer, CategoryModelSerializer
from rest_framework.permissions import AllowAny


class CategoryListAPIView(ListAPIView):
    queryset = CategoryModel.objects.all()
    serializer_class = CategoryModelSerializer
    permission_classes = [AllowAny, ]
    pagination_class = None


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
    queryset = BookModel.objects.all()
    serializer_class = BookModelSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ('title',)
    pagination_class = BooksPagination
