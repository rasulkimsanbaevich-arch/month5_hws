from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.ProductListCreat.as_view()),
    path('categories/', views.CategoryListCreat.as_view()),
    path('reviews/', views.ProductListCreat.as_view()),
    path('register/', views.RegisterUser.as_view())

]