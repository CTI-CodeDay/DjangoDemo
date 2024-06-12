from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True,null=True)
    made= models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=10000)
    summery = models.TextField()
    features = models.BooleanField () # null =True, defualt =True
