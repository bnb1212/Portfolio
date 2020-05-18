from django.shortcuts import render
from mysales.models import MySales

# Create your views here.
def Main(request):
    sangdata = MySales.objects.all()  # 장고의 ORM
    return render(request, 'main.html', {'sangdata':sangdata})  # forwarding
    
    class Meta:
        ordering = ('sang',)  # 반드시 tupletype
        ordering = ('sang', '-id')