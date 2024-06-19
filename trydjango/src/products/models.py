from django.db import models

# Create your models here.
class Product(models.Model):
    title       = models.CharField(max_length=120) # max_legnth is required
    description = models.TextField(blank=True, null=True)
    price       = models.DecimalField(decimal_places=2, max_digits=10000)
    summary     = models.TextField()
    featured    = models.BooleanField()  # null = True  or default = True