from django.db import models

# Create your models here.
class Producttab(models.Model):
    id = models.IntegerField(primary_key=True)
    category = models.CharField(max_length=20, blank=True, null=True)
    pname = models.CharField(max_length=20, blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    stock = models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'producttab'
