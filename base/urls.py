from django.contrib import admin
from django.urls import path
from .views import create_product, get_product, index, update_product, delete_product, get_Products, MyTokenObtainPairView, register
from .views import (get_categories, get_category, create_category, update_category, delete_category)

urlpatterns = [
    path('index', index),
    path('products', get_Products),
    path('product/<int:pk>/', get_product),
    path('product/add/', create_product, ),
    path('product/update/<int:pk>/', update_product,),
    path('product/delete/<int:pk>/', delete_product,),
    path('login', MyTokenObtainPairView.as_view()),
    path('register',register),
    # Category URLs
    path('categories', get_categories),
    path('category/<int:pk>/', get_category ),
    path('category/create/', create_category ),
    path('category/update/<int:pk>/', update_category ),
    path('category/delete/<int:pk>/', delete_category),
]