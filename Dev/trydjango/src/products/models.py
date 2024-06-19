from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=120) # with charfield, max_length attribute is required
    description = models.TextField(blank=True, null=True) # null=True allows database to hold an empty value for description
    #                                                       blank=True has to do with the field being blank itself
    #                                                       if blank=False --> field becomes required
    price = models.DecimalField(max_digits=10000, decimal_places=2)
    featured = models.BooleanField(null=True, default=True) #can include attributes: null=True, default=True or do it directly in
    #                                     terminal when you run the makemigrations
