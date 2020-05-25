from django.shortcuts import render
from myproduct.models import Producttab
from django.http.response import HttpResponse, HttpResponseRedirect
import json

# Create your views here.
def mainFunc(request):
    return render(request, 'main.html')

def adminFunc(request):
    return render(request, 'admin.html')

def productListFunc(request):
    category_no = request.GET.get('category')
    # 입력 테스트
    print(category_no)
    
    product_data = Producttab.objects.filter(category=category_no)
    
    # 빈 리스트 생성
    datas = [] 
    
    # 쿼리셋 -> 리스트[dict1, dict2, .... ]
    for s in product_data:
        dicData = {'id': s.id,
                   'category':s.category,
                   'pname':s.pname, 
                   'price':s.price,
                   'stock':s.stock,
                   'description':s.description}
        datas.append(dicData) 
        
    print(datas)
    
    # 값만을 넘겨줄 때에는 HttpResponse
    return HttpResponse(json.dumps(datas), content_type="application/json")

def adminListFunc(request):
    product_data = Producttab.objects.all()
    
    # 빈 리스트 생성
    datas = [] 
    
    # 쿼리셋 -> 리스트[dict1, dict2, .... ]
    for s in product_data:
        dicData = {'id': s.id,
                   'pname':s.pname, 
                   'category':s.category,
                   'price':s.price,
                   'stock':s.stock,
                   'description':s.description}
        datas.append(dicData) 
        
    print(datas)
    
    # 값만을 넘겨줄 때에는 HttpResponse
    return HttpResponse(json.dumps(datas), content_type="application/json")

def insertOkFunc(request):
    if request.method == 'POST':
        try:
            # 그룹 번호 구하기
            datas = Producttab.objects.all()
           
            if datas.count() != 0:
                # 데이터가 있다면 가장 마지막레코드(lastest) id + 1를 이렇게 쉽게 구할수 있다.
                id_new = Producttab.objects.latest('id').id + 1
            
            Producttab(
                id= id_new,
                pname=request.POST.get('pnameIns'),
                category=request.POST.get('categoryIns'),
                price=request.POST.get('priceIns'),
                stock=request.POST.get('stockIns'),
                description=request.POST.get('descriptionIns'),
            ).save()
                
        except Exception as e:
            print("insertOkFunc Error! :" + e)
            
    # 추가 후 목록 보기
    return HttpResponseRedirect('/ceo') 

def payFunc(request):
    p_data = Producttab.objects.get(id=request.GET.get('id'))
    
    print(p_data)
    p_data.stock = request.GET.get('quantity')
    p_data.save()
    
    datas = [] 
    
    # 쿼리셋 -> 리스트[dict1, dict2, .... ]
    dicData = {'id': p_data.id,
               'category':p_data.category,
               'pname':p_data.pname, 
               'price':p_data.price,
               'stock':p_data.stock,
               'description':p_data.description}
    datas.append(dicData) 
        
    print(datas)
    
    # 값만을 넘겨줄 때에는 HttpResponse
    return HttpResponse(json.dumps(datas), content_type="application/json")
    
def Update(request):
    name = request.GET.get('name')
    quantity = request.GET.get('quantity')
    
    order = Producttab.objects.get(pname=name)
    old_stock = Producttab.objects.filter(pname=name).values_list('stock')[0][0]
    new_stock = int(old_stock) - int(quantity)
    order.stock = new_stock
    try:
        order.save()
        result = {'result':'ok'}
    except:
        result = {'result':'booo'}
        
    return HttpResponse(json.dumps(result), 'application/json')