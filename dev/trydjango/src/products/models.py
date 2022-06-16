from django.db import models

# Create your models here.
# new Product class inherite Model class from basic models class in django
class Product(models.Model):
  title       = models.CharField(max_length=120)
  description = models.TextField(blank=True, null=True)
  price       = models.DecimalField(decimal_places=2, max_digits=1000)
  summary     = models.TextField(default='this is cool!')