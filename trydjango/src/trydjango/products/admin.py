from django.contrib import admin

# Register your models here.
# reletive import, it's importing the products_yash from moduls.py.
from .models import Product

admin.site.register(Product)