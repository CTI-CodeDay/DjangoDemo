from django.db import models

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=10000)
    summary = models.TextField(blank=True, null=False) # Allows us to leave summary empty (not requried)

    # null has to do with db while blank has to do with a required field or not


    featured = models.BooleanField() # null=True, default=True
    # default = 'this is cool!'