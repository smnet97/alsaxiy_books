from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response

from .models import BookModel
from .serializers import BookModelSerializer, BookModelDetailSerializer
from rest_framework.permissions import AllowAny


class BookDetailAPIView(RetrieveAPIView):
    permission_classes = [AllowAny, ]
    serializer_class = BookModelDetailSerializer
    queryset = BookModel.objects.all()

class BookModelListAPIView(ListAPIView):
    permission_classes = [AllowAny,]

    def list(self, request, *args, **kwargs):
        queryset = BookModel.objects.all()
        serializer = BookModelSerializer(queryset, many=True)
        return Response({
            'books': serializer.data
        })



