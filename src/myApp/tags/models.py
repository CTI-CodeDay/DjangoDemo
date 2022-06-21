from django.db import models

# Create your models here.
class Tag(models.Model): 
    company       = models.CharField(max_length=120)
    date          = models.DateField(blank=False)
    price         = models.DecimalField(decimal_places=2, max_digits=1000)
    driver        = models.CharField(blank=False, max_length=15)
    tagNumber     = models.CharField(blank=False, max_length=15)