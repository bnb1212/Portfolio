# 원격 DB - MariaDB와 연동

import MySQLdb
from docutils.nodes import danger
# conn = MySQLdb.connect(host='127.0.0.1', user='root', password='123', database='test')
# print(conn)
# conn.close

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
    conn = conn = MySQLdb.connect(**config)
    print(conn)
    cursor = conn.cursor()  # SQL문 수행을 위한 커서 객체 생성
    
    # 전체 자료 읽기
    sql = "select * from sangdata"
    cursor.execute(sql)
    
    # 부분 자료 읽기
    code=3
    sql = "select * from sangdata where code ='{0}'".format(code)
    cursor.execute(sql)
    
    
    # 출력 part1
    for data in cursor.fetchall():
        # print(data)
        print('%s %s %s %s' % data)
    print()
    
    # 출력 part2
    for r in cursor:
        # print(r)
        print(r[0], r[1], r[2], r[3])
    print()
    
    # 출력 part3
#     for (code, sang, su, dan) in cursor:
#         print(code, sang, su, danger

    print()
    # 출력4
    for(a,b,c,d) in cursor:
        print(a,b,c,d)
except Exception as err:
    print(err)
    
finally:
    cursor.close()
    conn.close()
                                                                                                                                                                                                                            
