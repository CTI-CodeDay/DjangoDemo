from django.db import models

# Create your models here.
class rats():
    name = models.TextField()
    hair_color= models.TextField()
    weight = models.TextField()
    summary = models.TextField(default = 'this is cool')
