from django.urls import *
from gtapp import views


# 요청이 다양하고 많을 경우 
urlpatterns = [
    path('insert', views.InsertFunc, name="InsertFunc"),
    
    ]
    
