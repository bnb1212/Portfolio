from django.db import models

# Create your models here.
class MySales(models.Model):
    sang = models.CharField(max_length=50)
    price = models.IntegerField()