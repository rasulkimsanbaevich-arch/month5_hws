from rest_framework import serializers
from .models import Review, Product, Category
from django.db.models import Avg

class CategoryDetailSerialize(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class CategorySerialize(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = 'id  name '.split()


class ProductDetailSerialize(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ReviewDetailSerialize(serializers.ModelSerializer):
    
    class Meta:
        model = Review
        fields = 'text stars'.split()

class ProductListSerialize(serializers.ModelSerializer):
    category = CategorySerialize(many=False)
    reviews = ReviewDetailSerialize(many=True)
    
    class Meta:
        model = Product
        fields = 'id title description category reviews average_rating'.split()
    



class ReviewSerialize(serializers.ModelSerializer):
    product = ProductListSerialize(many=False)
    class Meta:
        model = Review
        fields = 'id text stars product '.split()
