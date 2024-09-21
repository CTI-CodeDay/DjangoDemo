from django.contrib import admin
# Relative import, importing product class from models.py
from .models import Product

admin.site.register(Product)
