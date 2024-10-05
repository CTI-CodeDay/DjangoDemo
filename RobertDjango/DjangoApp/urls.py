from django.urls import path
from .views import product_list, product_detail  # Import your views

urlpatterns = [
    path('products/', product_list, name='product-list'),  # URL for product list
    path('products/<int:pk>/', product_detail, name='product-detail'),  # URL for product detail
]
