from django.shortcuts import render
from gogek import models
from django.http.response import HttpResponse
import json



# Create your views here.
def IndexFunc(request):
    return render(request, 'index.html')


def SearchFunc(request):    
    return render(request, 'search.html')


def ShowFunc(request):
    name = request.GET.get('name')
    tel = request.GET.get('tel')
    
    # join이 안되서 select를 여러번 했습니다.
    
    # name과 tel로 damsano를 get
    damsano = models.Gogek.objects.filter(gogek_tel=tel,gogek_name=name).values_list('gogek_damsano',)      
    jik_num = damsano[0][0]
    
    # 담사노로 직원 테이블의 부서번호를 get
    buser = models.Jikwon.objects.filter(jikwon_no=jik_num).values_list('buser_num',)       
    bu_num = buser[0][0]  
    
    # 직원과 부서의 data를 get 
    jikwon = models.Jikwon.objects.filter(jikwon_no=jik_num).all()
    buser = models.Buser.objects.filter(buser_no=bu_num).all()
    
    # json타입으로 만들기 위한 dict 생성
    context={
            'jikwon_name':jikwon[0].jikwon_name,
            'jikwon_jik':jikwon[0].jikwon_jik,
            'buser_name':buser[0].buser_name,
            'buser_tel':buser[0].buser_tel,
            'jikwon_gen':jikwon[0].jikwon_gen,
            'jikwon_ibsail':str(jikwon[0].jikwon_ibsail),
            'jikwon_rating':jikwon[0].jikwon_rating
        }
    # ajax에 값을 리턴할때 json 형식으로 보내기 때문에 json.dump을 썼다
    return HttpResponse(json.dumps(context), content_type="application/json")
    
    
