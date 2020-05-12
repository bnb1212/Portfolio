import MySQLdb
import sys

config = {  # dictionary 타입
    'host':'127.0.0.1',
    'user':'root',
    'password':'123',
    'database':'test',
    'port':3306,
    'charset':'utf8',
    'use_unicode':True
}

try:
    conn = MySQLdb.connect(**config)
    # print(conn)
    cursor = conn.cursor()  # SQL문 수행을 위한 커서 객체 생성
    
    # 부분 자료 읽기
    buser_num = input("부서 번호를 입력하세요 : ")
    #sql = "select jikwon_no, jikwon_name, buser_num, jikwon_jik from jikwon where buser_num ='{0}'".format(buser_num)
    #number_of_rows = cursor.execute(sql)
    
    # SQL 쿼리문이 길어질 경우
    sql = '''
    select jikwon_no, jikwon_name, buser_num, jikwon_jik 
    from jikwon 
    where buser_num ='{0}'
    '''.format(buser_num)    
    number_of_rows = cursor.execute(sql)
    
    
    if number_of_rows == 0:
        print(buser_num + "번 부서 사람은 없습니다")
        sys.exit()
    
    # 자료 출력
    print("사번\t이름\t부서번호\t직급")
    for data in cursor.fetchall():
        # print(data)
        print('%s\t%s\t%s\t\t%s' % data)
    print("인원수 : %d" % number_of_rows)
    print()
    
except Exception as err:
    print(err)
    
finally:
    cursor.close()
    conn.close()
    
