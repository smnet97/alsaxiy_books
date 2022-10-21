from django.shortcuts import render
from rest_framework import generics
from .models import UserModel
from .serializers import UserRegistrationSerializer
from rest_framework.permissions import AllowAny


class UserRegistrationView(generics.CreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = (AllowAny,)
