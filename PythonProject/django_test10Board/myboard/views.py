from django.shortcuts import render
from myboard.models import BoardTab
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http.response import HttpResponseRedirect
import datetime
from distributed.utils import get_ip


# Create your views here.
def mainFunc(request):
    # html 구문을 객체에 넣어 넘길수 있다.
    aa = "<div class='col-lg-3'>메뉴 3</div>"
    return render(request, 'main.html', {"main":aa})

# 목록보기
def listFunc(request):
    
    # 게시판 번호에 따라 정렬
    # datas = BoardTab.objects.all().order_by('-id')
    datas = BoardTab.objects.all().order_by('-gnum', 'onum')

    # 한 페이지당 5행 출력
    paginator = Paginator(datas, 5)
    page = request.GET.get('page')

    # 페이지 데이터 생성 및 예외 처리
    try:
        data = paginator.page(page)
    except PageNotAnInteger:
        data = paginator.page(1)
    except EmptyPage:
        data = paginator.page(paginator.num_pages())
        
    return render(request, 'board.html', {'data':data})


def insertFunc(request):
    return render(request, 'insert.html')

    
# 삽입 실행
def insertOkFunc(request):
    if request.method == 'POST':
        try:
            # 그룹 번호
            gbun = 1
            
            # 그룹 번호 구하기
            datas = BoardTab.objects.all()
            
            if datas.count() != 0:
                # 데이터가 있다면 가장 마지막레코드(lastest) id + 1를 이렇게 쉽게 구할수 있다.
                gbun = BoardTab.objects.latest('id').id + 1
                
            BoardTab(
                name=request.POST.get('name'),
                passwd=request.POST.get('passwd'),
                mail=request.POST.get('mail'),
                title=request.POST.get('title'),
                cont=request.POST.get('cont'),
                bip=request.META['REMOTE_ADDR'],
                bdate=datetime.datetime.now(),
                readcnt=0,
                gnum=gbun,
                onum=0,
                nested=0,
            ).save()
                
        except Exception as e:
            print("insertOkFunc Error! :" + e)
            
    # 추가 후 목록 보기
    return HttpResponseRedirect('/board/list') 


# 검색
def searchFunc(request):
    if request.method == "POST":
        s_type = request.POST.get('s_type')
        s_value = request.POST.get('s_value')
        # print(s_type, ' ', s_value)
        if s_type == 'title':
            # 칼렴명__contains는 
            datas = BoardTab.objects.filter(title__contains=s_value).order_by('-id') 
        elif s_type == 'name':
            datas = BoardTab.objects.filter(name__contains=s_value).order_by('-id')
            
        # 한 페이지당 5행 출력
    paginator = Paginator(datas, 5)
    page = request.GET.get('page')

    # 페이지 데이터 생성 및 예외 처리
    try:
        data = paginator.page(page)
    except PageNotAnInteger:
        data = paginator.page(1)
    except EmptyPage:
        data = paginator.page(paginator.num_pages())
        
    return render(request, 'board.html', {'data':data})


# 상세보기
def contentFunc(request):
    data = BoardTab.objects.get(id=request.GET.get('id'))
    
    # 조회수 증가
    data.readcnt = data.readcnt + 1
    data.save()

    page = request.GET.get('page')
    return render(request, 'content.html', {'data_one':data})

# 수정창 연결
def updateFunc(request):
    try:
        data = BoardTab.objects.get(id=request.GET.get('id'))
    except Exception as e:
        print("Update Error! : " + str(e))
        
    return render(request, 'update.html', {'data_one':data})

# 수정 실행
def updateOkFunc(request):
    if request.method == "POST":
        upRec = BoardTab.objects.get(id=request.POST.get('id'))
        
        # 비밀번호 검증
        if upRec.passwd == request.POST.get('up_passwd'):
            upRec.name = request.POST.get('name')
            upRec.mail = request.POST.get('mail')
            upRec.title = request.POST.get('title')
            upRec.cont = request.POST.get('cont')
            
            upRec.save()
        else:
            return render(request, 'error.html')
    
    # 수정후 목록보기
    return HttpResponseRedirect("/board/list")

# 삭제 접근
def deleteFunc(request):
    try:
        data = BoardTab.objects.get(id=request.GET.get('id'))
    except Exception as e:
        print("DeleteFunc Error! : " + str(e))

    return render(request, 'deleteok.html', {'data':data})

# 삭제 실행
def deleteOkFunc(request):
    if request.method == 'POST':
        delRec = BoardTab.objects.get(id=request.POST.get('id'))
        if delRec.passwd == request.POST.get('del_passwd'):
            delRec.delete()
            return HttpResponseRedirect('/board/list')
        else:
            return render(request, 'error.html')

# 댓글 접근
def replyFunc(request):
    try:
        redata = BoardTab.objects.get(id=request.GET.get('id'))
        
    except Exception as e:
        print("replyError! : " + str(e))
    return render(request, 'reply.html', {'data_one':redata})
        
        
# 댓글 실행
def replyOkFunc(request):
    if request.method == "POST":
        try:
            # 댓글의 그룹 넘버 / 정렬 넘버
            re_gnum = int(request.POST.get('gnum'))
            re_onum = int(request.POST.get('onum'))
            
            tempRec = BoardTab.objects.get(id = request.POST.get('id'))
            old_gnum = tempRec.gnum
            old_onum = tempRec.onum
            
            if old_gnum >= re_onum and old_gnum == re_gnum:
                
                # onum 갱신
                old_onum = old_onum + 1
                
            BoardTab(
                name=request.POST.get('name'),
                passwd=request.POST.get('passwd'),
                mail=request.POST.get('mail'),
                title=request.POST.get('title'),
                cont=request.POST.get('cont'),
                bip=request.META['REMOTE_ADDR'],
                bdate=datetime.datetime.now(),
                readcnt=0,
                gnum=re_gnum,
                onum=old_onum,
                nested= int(request.POST.get('nested')) +1,
            ).save()
                
        except Exception as e:
            print("replyOkFunc Error! :" + str(e))
            
    # 추가 후 목록 보기
    return HttpResponseRedirect('/board/list') 
        
        