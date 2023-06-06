from django.contrib import admin

# Register your models here.
from .models import Product # relatively import models.py
admin.site.register(Product)