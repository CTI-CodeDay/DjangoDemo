from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length = 120) #max_length is required
    discription = models.TextField(blank = True,null = True)
    price = models.DecimalField(decimal_places = 2, max_digits = 10000)
    summary = models.TextField()
    #when we migrate but add a new field this will cause an error
    #this is why we use the null argument, as when if we add more products and they dont have that field
    #it will added but left null, or we can make it default have a default value
    #this default can be assigned to products already in the database no issue
    featured = models.BooleanField()