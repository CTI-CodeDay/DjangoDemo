from django.db import models

# Create your models here.
class Poll(models.Model):
    topic = models.CharField(max_length=120, blank=False)
    description = models.TextField(blank=False)
    trend = models.DecimalField(decimal_places=2, max_digits=4)
    active = models.BooleanField(default=False)