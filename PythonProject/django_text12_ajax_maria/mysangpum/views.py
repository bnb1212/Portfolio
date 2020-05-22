from django.shortcuts import render
from mysangpum.models import Sangdata
import json
from django.http.response import HttpResponse

# Create your views here.
def mainFunc(request):
    return render(request, "main.html")

# 목록 페이지 부르기
def listFunc(request):
    return render(request, 'list.html')

# 데이터 불러 넘겨주기
def showDataFunc(request):
    # DB에서 리스트 받음
    s_data = Sangdata.objects.all()
    
    # 빈 리스트 생성
    datas = [] 
    
    # 쿼리셋 -> 리스트[dict1, dict2, .... ]
    for s in s_data:
        dicData = {'code': s.code, 'sang':s.sang, 'su':s.su, 'dan':s.dan}
        datas.append(dicData) 
        
    print(datas)
    
    # 값만을 넘겨줄 때에는 HttpResponse
    return HttpResponse(json.dumps(datas), content_type="application/json")