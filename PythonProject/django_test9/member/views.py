from django.shortcuts import render
from member.models import MemTable
import MySQLdb
from django.http.response import HttpResponseRedirect

config = {
    'host':'127.0.0.1',
    'user':'root',
    'password':'123',
    'database':'dbmember',
    'port':3306,
    'charset':'utf8',
    'use_unicode':True
    
    }
# Create your views here.
def main(request):
    return render(request, 'main.html')


def listFunc(request):
    datas = MemTable.objects.all()
    print(datas)
    return render(request, 'list.html', {'members':datas})


# Insert폼 띄우기 / 삽입 실행
def insertFunc(request):
    if request.method == 'GET':
        return render(request, 'insert.html')
    elif request.method == 'POST':
        MemTable(
            memid = request.POST.get('memid'),
            passwd = request.POST.get('passwd'),
            name = request.POST.get('name'),
            email = request.POST.get('email'),
            phone = request.POST.get('phone'),
            zipcode = request.POST.get('zipcode'),
            address = request.POST.get('address'),
            job = request.POST.get('job'),
            ).save()
            
        return HttpResponseRedirect('/member/list')
    else:
        return render(request, 'error.html')

def idCheckFunc(request):
    memid = request.GET.get('memid')
    
    # 해당 id 회원 등록 여부 판단
    isRegister = False 
        
    try:
        # 방법 1 : ORM
        # data = MemTable().objects.get(memid=memid)
        # print('data :' , data)
        # isRegister= True
        
        # 방법 2 : sql
        conn = MySQLdb.connect(**config)
        sql = "select * from member_memtab where memid ='{}'".format(memid)
        cursor = conn.cursor()
        cursor.execute(sql)
        data = cursor.fetchone()
        # pirint('data : ', data) # data가 없으면 ㅒNone
        
    except Exception as e:
        print('idCheckFunc error : ' + str(e))
        
        
    finally:
        cursor.close()
        conn.close()
        
    return render(request, 'idcheck.html', {'memid':isRegister})
    
# 우편번호 찾기 창 띄우기
def zipCheckFunc(request):
    chk = request.GET.get('check')
    return render(request, 'zipcheck.html', {"check" : chk})

# 우편번호 찾기 작업 실행
def zipCheckOkFunc(request):
    area3 = request.POST.get('area3')
    
    #try-except 쓰는게 정석
    conn = MySQLdb.connect(**config)
    sql = "select * from member_ziptab where area3 like'{}%'".format(area3)
    cursor = conn.cursor()
    cursor.execute(sql)
    datas = cursor.fetchall()
    
#     print(datas)
    cursor.close()
    conn.close()
    
    return render(request, 'zipcheck.html', {'datas':datas, 'check':'n'})

    