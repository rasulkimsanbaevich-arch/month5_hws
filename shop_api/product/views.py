from django.shortcuts import render
from .models import Category, Product, Review
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.forms import model_to_dict 
from rest_framework import status
from product import serialize
# Create your views here.

@api_view(["GET"])
def category_detail(request, id):
    try:
        review = Category.objects.get(id=id)
    except Category.DoesNotExist:
        return Response(
            data={"text": "not found"},
            status=status.HTTP_404_NOT_FOUND
        )
    data = serialize.CategoryDetailSerialize(review, many=False).data
    return Response(
        data=data
    )
@api_view(http_method_names=['GET'])
def list_api_category(request):
    categories = Category.objects.all()
    data = serialize.CategorySerialize(categories, many=True).data

    return Response(
        data=data
    )


@api_view(["GET"])
def product_detail(request, id):
    try:
        review = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return Response(
            data={"text": "not found"},
            status=status.HTTP_404_NOT_FOUND
        )
    data = serialize.ProductDetailSerialize(review, many=False).data
    return Response(
        data=data
    )
@api_view(http_method_names=['GET'])
def product_api_list(request):
    products = Product.objects.all()
    
    data = serialize.ProductListSerialize(products, many=True).data

    return Response(
        data=data
    )
@api_view(["GET"])
def review_detail(request, id):
    try:
        review = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(
            data={"text": "not found"},
            status=status.HTTP_404_NOT_FOUND
        )
    data = serialize.ReviewDetailSerialize(review, many=False).data
    return Response(
        data=data
    )
@api_view(http_method_names=['GET'])
def review_list(request):
    reviews = Review.objects.all()
    data = serialize.ReviewSerialize(reviews, many=True).data
    return Response(
        data=data
    )



    