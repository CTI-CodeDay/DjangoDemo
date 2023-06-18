from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)  # Price should typically be a decimal, not a text field
    summary = models.TextField()
