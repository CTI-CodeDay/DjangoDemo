from django.db import models

# Create your models here.
class Product(models.Models):
    title = models.TextField()
    description = models.TextField()
    price = models.TextFields()