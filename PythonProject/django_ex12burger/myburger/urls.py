from django.urls import path
from myburger import views

urlpatterns = [
    path('main', views.Main),
    path('menus', views.Menu),
    path('update', views.Update),
    path('admin', views.Admin),
    path('show', views.Show),
    path('insert', views.Insert),
    
]
