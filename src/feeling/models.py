from django.db import models

# Create your from django.db import models

class Product(models.Model):
    title = models.TextField()
    description = models.TextField()
    price = models.TextField()
    summary = models.TextField()
