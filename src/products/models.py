from django.db import models

# Create your models here.
class Product(models.Model):
  title = models.CharField(max_length=128)
  description = models.TextField(blank=True)
  price = models.DecimalField(decimal_places = 2, max_digits=100000)
  summary = models.TextField(blank=True, null=False)
  featured = models.BooleanField(default=False)