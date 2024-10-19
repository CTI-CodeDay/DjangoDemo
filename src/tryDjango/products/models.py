from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length = 100, default = "Item")
    summary = models.TextField(default = "This is an item")
    description = models.TextField(default = "About this item")
    price = models.DecimalField(default = 0.00, max_digits = 7, decimal_places = 2)
    