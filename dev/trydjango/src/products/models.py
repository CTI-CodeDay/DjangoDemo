from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.TextField(max_length = 120)
    description = models.TextField(blank = True, null True)
    price = models.TextField(default = 'this is cool!')
    