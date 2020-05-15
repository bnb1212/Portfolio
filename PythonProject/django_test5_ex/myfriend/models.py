from django.db import models

# Create your models here.
class Friends(models.Model):
    name = models.CharField(max_length=10)
    addr = models.CharField(max_length=20)
    age = models.IntegerField()
    
    