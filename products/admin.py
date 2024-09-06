from django.db import models

# Create your models here.
class Product(models.Model):  # Inherit from models.Model
    title = models.TextField()
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Use DecimalField for price
    summary = models.TextField(default="This is cool")

    def __str__(self):
        return self.title

from django.contrib import admin

# Register your models here.
admin.site.register(Product)