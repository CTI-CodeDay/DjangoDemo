from django.db import models

# Create your models here.
# new Product class inherite Model class from basic models class in django
class Product(models.Model):
  title       = models.TextField()
  description = models.TextField()
  price       = models.TextField()