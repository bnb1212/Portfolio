from django.shortcuts import render
from myguest.models import Guest
from django.http.response import HttpResponseRedirect
from datetime import datetime


# Create your views here.
def MainFunc(request):
    return render(request, 'main.html')

    
def ListFunc(request):
    gdata = Guest.objects.all()  # 장고의 ORM
#    gdata = Guest.objects.all().order_by()
#    gdata = Guest.objects.all().order_by()
    # gdata = Guest.objects.all().order_by('-title') # decending sort
    # gdata = Guest.objectes.all().order_by('-id')[0:2]
    return render(request, 'list.html', {'gdata':gdata})  # forwarding
    
    class Meta:
        ordering = ('title',)  # 반드시 tupletype
        ordering = ('title', '-id')

        
def InsertFunc(request):
    return render(request, 'insert.html')


def InsertOkFunc(request):
    if request.method == 'POST':
        # print(request.POST['title'])
        # print(request.POST.get('title'))
        
        # ORM의 insert/update
        Guest(
            title=request.POST['title'],
            content=request.POST['content'],
            regdate=datetime.now(),
            
            ).save()  
        
        return HttpResponseRedirect('/guest')
    else :
        return HttpResponseRedirect('/guest/insert')
