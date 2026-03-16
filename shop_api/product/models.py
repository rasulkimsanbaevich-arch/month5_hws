from django.db import models
from django.forms import model_to_dict
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
    
class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='productss')

    def __str__(self):
        return self.title
    
    
    def average_rating(self):
        reviews = self.reviews.all()
    
        total = 0
        count = 0

        for review in reviews:
            total += review.stars
            count += 1

        if count == 0:
            return 0

        return total / count
    
        
    
STARS = ((i, '*' * i)for i in range(1, 5+1))
    
class Review(models.Model):
    text = models.TextField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="reviews")
    stars = models.IntegerField(choices=STARS, default=0, null=True)

    def __str__(self):
        return self.text
    
    
    

    
    
