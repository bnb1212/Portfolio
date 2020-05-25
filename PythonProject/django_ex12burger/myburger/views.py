from django.shortcuts import render
from myburger import models
from django.http.response import HttpResponse , HttpResponseRedirect
import json
from django.utils import encoding
from myburger.models import Producttab


# Create your views here.
def Index(request):
    return render(request, 'index.html')


def Main(request):
    return render(request, 'main.html')

# 메뉴 보여주기
def Menu(request):
    
    menu = request.GET.get('menu') 
   
    data = models.Producttab.objects.all().filter(category=menu)
    datas = []
    for i in range(len(data)):
        content = {
            'id':data[i].id,
            'category':data[i].category,
            'pname':data[i].pname,
            'price':data[i].price,
            'stock':data[i].stock,
            'description':data[i].description
        }
        datas.append(content)
    
    return HttpResponse(json.dumps(datas), 'application/json')


## 이름과 수량을 가져와 업데이트를 하고 성공 실패 여부를 돌려주는 함수
def Update(request):
    name = request.GET.get('name')
    quantity = request.GET.get('quantity')
    order = models.Producttab.objects.get(pname=name)
    old_stock = models.Producttab.objects.filter(pname=name).values_list('stock')[0][0]
    new_stock = int(old_stock) - int(quantity)
    order.stock = new_stock
    try:
        order.save()
        result = {'result':'ok'}
    except:
        result = {'result':'booo'}
        
    return HttpResponse(json.dumps(result), 'application/json')

## 관리자로 가기
def Admin(request):
    return render(request, 'admin.html')

# 데이터 보여주기
def Show(request):
    
    data = models.Producttab.objects.all()
    datas = []
    for i in range(len(data)):
        
        content = {
            'id':data[i].id,
            'category':data[i].category,
            'pname':data[i].pname,
            'price':data[i].price,
            'stock':data[i].stock,
            'description':data[i].description
        }
        datas.append(content)
        
    return HttpResponse(json.dumps(datas), 'application/json')

# 상품등록하기
def Insert(request):
    
    id = request.GET.get('id')
    category = request.GET.get('category')
    pname = request.GET.get('pname')
    price = request.GET.get('price')
    stock = request.GET.get('stock')
    description = request.GET.get('description')
    '''
    print(id)
    print(category)
    print(pname)
    print(price)
    print(stock)
    '''    
    product = Producttab()
    product.id = id
    product.category = category
    product.pname = pname
    product.price = price
    product.stock = stock
    product.description = description
    product.save()
    
    return HttpResponseRedirect('/order/admin')
    
    
