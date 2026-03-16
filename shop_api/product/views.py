from django.shortcuts import render
from .models import Category, Product, Review
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.forms import model_to_dict 
from rest_framework import status
from product import serialize
# Create your views here.

# Category
@api_view(["GET", "PUT", "DELETE"])
def category_detail(request, id):
    
    try:
        category = Category.objects.get(id=id)
    except Category.DoesNotExist:
        return Response(
                data={"text": "not found"},
                status=status.HTTP_404_NOT_FOUND
            )
    if request.method == "GET":
        data = serialize.CategoryDetailSerialize(category, many=False).data
        return Response(
            data=data
            )
    elif request.method == "DELETE":

        category.delete()
        return Response(
            status=status.HTTP_204_NO_CONTENT
        )
    elif request.method == "PUT":
        category.name = request.data.get("name")
        category.save()
        return Response(
            data=serialize.CategoryDetailSerialize(category).data,
            status=status.HTTP_201_CREATED
        )
@api_view(http_method_names=['GET', 'POST'])
def list_api_category(request):
    if request.method == "GET":
        categories = Category.objects.all()
        data = serialize.CategorySerialize(categories, many=True).data

        return Response(
            data=data
        )
    elif request.method == "POST":
        serializer = serialize.CategoryValidateSerialize(data=request.data)
        if not serializer.is_valid():
            return Response(
                data=serializer.errors,
                status=status.HTTP_400_BAD_REQUEST,
            )
        
        name = serializer.validated_data.get("name")
        category = Category.objects.create(
            name=name
        )
        return Response(
            data=serialize.CategorySerialize(category).data,
            status=status.HTTP_201_CREATED
        )

# Products
@api_view(["GET", "PUT", "DELETE"])
def product_detail(request, id):
    try:
        product = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return Response(
            data={"text": "not found"},
            status=status.HTTP_404_NOT_FOUND
        )
    if request.method == "GET":
        data = serialize.ProductDetailSerialize(product, many=False).data
        return Response(
            data=data
        )
             
    elif request.method == "DELETE":

        product.delete()
        return Response(
            status=status.HTTP_204_NO_CONTENT
        )
    elif request.method == "PUT":
        product.title = request.data.get("title")
        product.description = request.data.get("description")
        product.price = request.data.get("price")
        product.category_id = request.data.get("category_id")
        product.save()
        return Response(
            data=serialize.ProductDetailSerialize(product).data,
            status=status.HTTP_201_CREATED
        )
@api_view(http_method_names=['GET', 'POST'])
def product_api_list(request):
    if request.method == "GET":
        products = Product.objects.all()
        data = serialize.ProductListSerialize(products, many=True).data

        return Response(
        data=data
    )

    elif request.method == "POST":
        serializer = serialize.ProductValidateSerialize(data=request.data)
        if not serializer.is_valid():
            return Response(
                data=serializer.errors,
                status=status.HTTP_400_BAD_REQUEST,
            )
        title = serializer.validated_data.get("title")
        description = serializer.validated_data.get("description")
        price = serializer.validated_data.get("price")
        category_id = serializer.validated_data.get("category_id")
        review = Product.objects.create(
            title=title,
            description=description,
            price=price,
            category_id=category_id
        )
        return Response(
            data=serialize.ProductListSerialize(review).data,
            status=status.HTTP_201_CREATED
        )

# Reviews 
@api_view(["GET", "PUT", "DELETE"])
def review_detail(request, id):
    try:
        review = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(
            data={"text": "not found"},
            status=status.HTTP_404_NOT_FOUND
        )
    if request.method == "GET":
        data = serialize.ReviewDetailSerialize(review, many=False).data
        return Response(
            data=data
        )
    elif request.method == "DELETE":

        review.delete()
        return Response(
            status=status.HTTP_204_NO_CONTENT
        )
    elif request.method == "PUT":
        review.text = request.data.get("text")
        review.stars = request.data.get("stars")   
        review.product_id = request.data.get("product_id") 
        review.save()
        return Response(
            data=serialize.ReviewDetailSerialize(review).data,
            status=status.HTTP_201_CREATED
        )
@api_view(http_method_names=['GET', 'POST'])
def review_list(request):
    if request.method == "GET":
        reviews = Review.objects.all()
        data = serialize.ReviewSerialize(reviews, many=True).data
        return Response(
            data=data
        )
    elif request.method == "POST":
        serializer = serialize.ReviewValidateSerialize(data=request.data)
        if not serializer.is_valid():
            return Response(
                data=serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )
        
        text = request.data.get("text")
        stars = request.data.get("stars")
        product_id = request.data.get("product_id")
        review = Review.objects.create(
            text= text,
            stars=stars,
            product_id=product_id
        )
        return Response(
            data=serialize.ReviewSerialize(review).data,
            status=status.HTTP_201_CREATED
        )
    


    