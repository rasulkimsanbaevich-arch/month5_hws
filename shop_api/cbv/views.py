from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from product import models
from product import serialize
from . import serializer
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.views import APIView

class ProductListCreat(ListCreateAPIView):
    queryset = models.Product.objects.all()
    serializer_class = serialize.ProductListSerialize

class CategoryListCreat(ListCreateAPIView):
    queryset = models.Category.objects.all()
    serializer_class = serialize.CategorySerialize

class ReviewListCreat(ListCreateAPIView):
    queryset = models.Review.objects.all()
    serializer_class = serialize.ReviewSerialize

class RegisterUser(APIView):
    serializer_class = serializer.Register
    def post(self, request):
        serialize = self.serializer_class(data=request.data)
        serialize.is_valid(raise_exception=True)
        User.objects.create_user(**serialize.validated_data)
        return Response(data={"text": "User is created!"}, status=status.HTTP_201_CREATED)

class Authentication(APIView):
    authentication_classes = []