from django.shortcuts import render
from myjikwon.models import Jikwon, Buser, Gogek
from django.db.models import Count, functions
from django.db.models.expressions import Subquery, OuterRef
from django.db.models.aggregates import Sum, Max

# Create your views here.
def MainFunc(request):
    buser_data = Buser.objects.all()
    return render(request, 'main.html', {'busers':buser_data})

def JikFunc(request):
    jik_data_all = Jikwon.objects.all()
    
    # 고객테이블에서 담당사원번호 끼리 그룹
#     gogek_data = Gogek.objects.filter(
#         gogek_damsano=Subquery(Jikwon.objects.filter(jikwon_no=OuterRef('gogek_damsano'))
#                                .values('jikwon_no')
#                                )
#         ).values('gogek_damsano').annotate(count=Count('gogek_damsano'))
#     
    
    jik_data = jik_data_all.filter(buser_num=request.GET.get('buser_no'))
    
    # JOIN ( Foreign Key 기반 )
    jik_data_j = jik_data.select_related().annotate(count=Count('gogek')) # Max('gogek_no')
    jik_test = jik_data.select_related()
    
    # select_related()를 하면 외래키를 바탕으로 PK키를 가져온다.
    
#     print(jik_test.query)
#     print(jik_data_j.query)
#     print(jik_data)
    return render(request, 'jiklist.html', {'jikwons':jik_data_j})

def GogekFunc(request):
    
    gogek_data_all = Gogek.objects.all().order_by('gogek_name')
    gogek_data = gogek_data_all.filter(
                gogek_damsano=request.GET.get('jikwon_no')
                ).annotate(
                gender=functions.Substr('gogek_jumin',8,1))
    return render(request, 'gogeklist.html', {'gogeks':gogek_data})



