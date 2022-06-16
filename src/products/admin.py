from django.contrib import admin

#relative import 
from .models import Product

admin.site.register(Product)