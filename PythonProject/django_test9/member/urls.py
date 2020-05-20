from django.urls import path
from member import views

urlpatterns = [
    path('list/', views.listFunc),
    path('insert', views.insertFunc),
    path('insertok', views.insertFunc),
    path('idcheck', views.idCheckFunc),
    path('zipcheck', views.zipCheckFunc),
    path('zipcheckok', views.zipCheckOkFunc),
    
    
    ]