from django.shortcuts import render
import json
from django.http.response import HttpResponse

lan = {
    'id':111,
    'name':'파이썬',
    'history':[
        {'date':'2020-5-20', 'exam':'basic'},
        {'date':'2020-5-21', 'exam':'django'},
        ]
    }

# Create your views here.


# json 연습
def good():
    
    print(type(lan))  # 결과 : <class 'dict'>
    
    # JSON 인코딩(encoding)
    jsonString = json.dumps(lan)
    
    print(jsonString, ' ', type(jsonString)) 
    # 결과 :{"id": 111, "name": "\ud30c\uc774\uc36c", "history": [{"date": "2020-5-20", "exam": "basic"}, {"date": "2020-5-21", "exam": "django"}]}   <class 'str'> 
    
    # indent arg를 주면 들여쓰기가 된다 값을 주는 만큼 들여쓰기 많이한다.
    jsonString = json.dumps(lan, indent=4)
    print(jsonString)
    
    print()
    
    # JSON 디코딩(decoding) --str ==> python object ----------
    dic = json.loads(jsonString)
    print(dic)
    print(type(dic))  # 결과 : <class 'dict'>
    print(dic['name'])
    for h in dic['history']:
        print(h['date'], ' ', h['exam'])


# AJAX 연습
def ajaxFunc1(request):
    msg = request.GET['msg']
    print(msg, type(msg))  # 결과 : {'key':'~~'} <class 'dict'>
    context = {'key':msg}
    print(context, type(context))  # 결과 
    
    print(json.dumps(context), ' ', type(json.dumps(context)))
    
    # 데이터 값만 넘길때는 HttpResponse로 하면 된다.
    return HttpResponse(json.dumps(context), content_type="application/json")


def mainFunc(request):
#     good()
    
    return render(request, 'main.html')
    
