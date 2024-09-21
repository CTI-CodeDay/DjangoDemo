from django.db import models

# Create your models here.
# "I want my backend to store memory of a product"
# ^ Make this happen in this file.

class Product(models.Model):
    title       = models.CharField(max_length=120) # max_length required for CharField, if you try doing python manage.py makemigrations it will cause an error.
    description = models.TextField(blank=True, null=True)
    price       = models.DecimalField(decimal_places=2, max_digits=100)
    summary     = models.TextField(blank=True, null=True)
    featured    = models.BooleanField() # When adding this model, the products already created won't have this value yet. You can use default=True/False, null=True/False