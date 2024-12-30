from django.contrib import admin
from .models import Product     #relative import (in same directory)

# Register your models here.
admin.site.register(Product)
