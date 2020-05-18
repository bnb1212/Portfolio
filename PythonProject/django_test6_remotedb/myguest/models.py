from django.db import models

# Create your models here.
class Guest(models.Model):
    # mariaDB에 맞게 테이블에 만들어진다 ( 장고의 강점 ) 
    title = models.CharField(max_length=50)
    content = models.TextField()
    regdate = models.DateTimeField()
    
