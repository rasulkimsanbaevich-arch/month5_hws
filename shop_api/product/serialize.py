from rest_framework import serializers
from .models import Review, Product, Category
from rest_framework.exceptions import ValidationError

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
        fields = 'title description'.split()

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
    product = ProductDetailSerialize(many=False)
    class Meta:
        model = Review
        fields = 'id text stars product '.split()

# Validations

class CategoryValidateSerialize(serializers.Serializer):
    name = serializers.CharField()



class ProductValidateSerialize(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    description = serializers.CharField(default="Something description")
    price = serializers.IntegerField()
    category_id = serializers.IntegerField()

    def validate_category_id(self, category_id):
        try:
            Category.objects.get(id=category_id)
        except Category.DoesNotExist:
            raise ValidationError("Category_id doesnot exists!")
        return category_id
        


class ReviewValidateSerialize(serializers.Serializer):
    text = serializers.CharField()
    stars = serializers.IntegerField(min_value=1, max_value=10)
    product_id = serializers.IntegerField()
    
    def validate_product_id(self, product_id):
        try: 
            Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            raise ValidationError("Product_id doesnot exists!")
        return product_id