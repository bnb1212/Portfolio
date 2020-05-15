from django.shortcuts import render
from myapp.models import Article

# Create your views here.
def Main(request):
    return render(request, 'main.html')

def Dbtest(request):
    datas = Article.objects.all() # Django의 ORM 
    # = select * from Ariticle
    # 여기서 Article은 사실 myapp_article 이다.
    
    # print(datas[0].sang)
    
    return render(request,'articlelist.html', {'articles':datas})
    
    
    