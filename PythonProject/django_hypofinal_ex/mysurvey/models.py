from django.db import models

# Create your models here.
class Surveydata(models.Model):
    job = models.CharField(max_length=20)
    gender = models.CharField(max_length=10)
    game_time = models.FloatField()