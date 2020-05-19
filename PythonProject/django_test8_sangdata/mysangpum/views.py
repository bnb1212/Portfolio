from django.shortcuts import render
from mysangpum.models import Sangdata
from django.http.response import HttpResponseRedirect
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

# Create your views here.


def MainFunc(request):
    return render(request, 'main.html')


# 목록 출력
def ListFunc(request):
    '''
    conn = ""
    sql = "select * from sangdata"
    
    cursor = conn.cursor()
    cursor.execute(sql)
    datas = cursor.fetchall()    # 이렇게 직접 sql 쿼리문을 적어줄 경우 받는 
                                 # html에서는 {{key.0}} {{key.1}} 식으로 받아 써야한다. 
                                 # ( 반환형이 tuple)
    '''
    # ORM은 세밀한 sql 쿼리문을 적기에는 한계가 있다.
    
    # sangdatas = Sangdata.objects.all()  # ORM의 리턴 타입(return type)은 QuerySet이다.
    
    # return render(request, 'list.html', {'sangpums':sangdatas})

    # 페이지 나누기 기능은 list2.html로 출력하기
    sangdatas = Sangdata.objects.all().order_by('-code') # 컬럼명 앞에 - 붙으면 descending sort(내림차순)

    # 페이지를 나누어 주는 paginator 페이지네이터
    paginator = Paginator(sangdatas, 5)
    
    try:
        page = request.GET.get('page')
    except:
        page = 1
    
    try:
       data = paginator.page(page)
        
    # 페이지가 정수가 아닌 경우
    except PageNotAnInteger:
        data = paginator.page(1)
    # 페이지가 받아지지 않은경우
    except EmptyPage:
        data = paginator.page(paginator.num_pages())
    
        # 개별 페이지 표시용 작업
    
    allpage = range(paginator.num_pages + 1) 
    # print('allpage:', allpage)
    
    return render(request, 'list2.html', {'sangpums':data, 'allpage':allpage})
    
# 삽입 창
def InsertFunc(request):
    return render(request, 'insert.html')


# 삽입 확인
def InsertOkFunc(request):
    # code 중복 체크가 필요하나 생략
    
    if request.method == 'POST':
#         print(request.POST.get('sang'))
        Sangdata(
            code = request.POST.get('code'),
            sang = request.POST.get('sang'),
            su = request.POST.get('su'),
            dan = request.POST.get('dan'),
            ).save()

        return HttpResponseRedirect('list')
# 수정 창 
def UpdateFunc(request):
    data = Sangdata.objects.get(code=request.GET.get('code'))
    return render(request, 'update.html', {'sang_one':data})


# 수정 확인
def UpdateOkFunc(request):
    if request.method == 'POST':
        upRec = Sangdata.objects.get(code=request.POST.get('code'))
        upRec.code = request.POST.get('code')
        upRec.sang = request.POST.get('sang')
        upRec.su = request.POST.get('su')
        upRec.dan = request.POST.get('dan')
        
        upRec.save() # 수정 완료
        
    return HttpResponseRedirect('list')

# 삭제
def DeleteFunc(request): # try - except 안에서 하는 것이 정석임.
    delRec = Sangdata.objects.get(code=request.GET.get('code'))
    delRec.delete()
    
    return HttpResponseRedirect('list')
