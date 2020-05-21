from django.urls import path
from gogek import views

urlpatterns = [
    path('search',views.SearchFunc),
    path('show',views.ShowFunc),
]
