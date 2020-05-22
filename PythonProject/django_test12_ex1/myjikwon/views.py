from django.shortcuts import render
from myjikwon.models import Jikwon, Buser
from django.db.models.expressions import Subquery, OuterRef
from django.http.response import HttpResponse
import json

# Create your views here.
def mainFunc(request):
    return render(request, 'main.html')

# 목록 검색 메인
def listFunc(request):
    return render(request, 'list.html')

# 검색버튼 기능
def searchFunc(request):
    jik_rank = request.GET.get('frm_jik')
    # 입력 테스트
    print(jik_rank)
    
    jik_data = Jikwon.objects.filter(jikwon_jik=jik_rank
                                     ).annotate(buser_name=Subquery(Buser.objects.filter(buser_no=OuterRef('buser_num')).values('buser_name')[:1]))
    
    # jikdata test                                 
    print(jik_data)
    
    # 빈 리스트 생성
    datas = [] 
    
    # 쿼리셋 -> 리스트[dict1, dict2, .... ]
    for s in jik_data:
        dicData = {'jikwon_no': s.jikwon_no,
                   'jikwon_name':s.jikwon_name, 
                   'buser_name':s.buser_name}
        datas.append(dicData) 
        
    print(datas)
    
    # 값만을 넘겨줄 때에는 HttpResponse
    return HttpResponse(json.dumps(datas), content_type="application/json")