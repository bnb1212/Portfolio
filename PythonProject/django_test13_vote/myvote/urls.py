from django.urls import path
from myvote import views

urlpatterns = [
    path('',views.DispFunc, name='disp'),
    # <int: ~ >
    path('<int:question_id>/',views.DetailFunc, name='detail'),
    path('<int:question_id>/vote',views.VoteFunc, name='vote'),
    path('<int:question_id>/result',views.ResultFunc, name='results'),

    
]
