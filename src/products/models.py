from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=100) # max_length is required
    description = models.TextField(blank = True,null=True)
    price = models.DecimalField(max_digits=100,decimal_places=2)
    summary = models.TextField(blank = True,null = False) # For required fields - set blank = True
    featured = models.BooleanField() #null = True ,  defualt = True
