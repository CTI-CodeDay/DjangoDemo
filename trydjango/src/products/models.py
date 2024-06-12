from django.db import models

# Create your models here.
# backend to have memory of 

class Product(models.Model):
    # title, description, price
    title = models.CharField(max_length=120) # max length is required
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=1000)
    summary = models.TextField(blank=False, null=False)
    # featured = models.BooleanField(null=True) #empty can be true
    featured = models.BooleanField() #null=True, default=True

