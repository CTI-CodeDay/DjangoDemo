from django.db import models
# whenever we make changes to models.py
# call python manage.py makemigrations & migrate

# Create your models here.
class Product(models.Model):
    title       = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    price       = models.DecimalField(max_digits=200, decimal_places=2)
    summary     = models.TextField(blank=False, null=False) # blank = False = required # null = required
    featured    = models.BooleanField()