from django.db import models

# Create your models here.
class TestModel(models.Model):
    title = models.TextField(default="Bruh")
    desc = models.TextField(default="very cool items")
    price = models.BigIntegerField(default=69.99)
    date = models.DateField(default="1111-01-01")