from rest_framework import serializers
from .models import Review, Product, Category


class CategoryDetailSerialize(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
class ProductDetailSerialize(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
class ReviewDetailSerialize(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
class ReviewSerialize(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'id title price description'.split()