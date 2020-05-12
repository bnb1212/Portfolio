# 원격 DB - MariaDB와 연동

import MySQLdb
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
    # print(conn)
    cursor = conn.cursor()  # SQL문 수행을 위한 커서 객체 생성
    
    # 전체 자료 읽기
    '''
    sql = "select * from sangdata"
    cursor.execute(sql)
    '''
    # 부분 자료 읽기
    code = 3
    sql = "select * from sangdata where code ='{0}'".format(code)
    cursor.execute(sql)
    
    # 자료 추가
    '''
    # sql = "insert into sangdata (code, sang, su, dan) values(13, '상품1', 3, 1000)"
    # cursor.execute(sql)
    # conn.commit() # 파이썬은 기본적으로 CRUD 작업후 commit
    
    sql = "insert into sangdata values (%s, %s, %s, %s)"
    sql_data = ('14', '신상2', 5, 2000) # Tuple 형식으로 데이터 삽입
    # sql_data = '14', '신상2', 5, 2000
    cursor.execute(sql, sql_data)
    conn.commit()
    '''
    
    # ===== 자료 수정 ===== 
    '''
    sql = "update sangdata set sang=%s, su=%s, dan=%s where code=%s"
    sql_data = ('파이썬', '7', '7000', '14')
    cursor.execute(sql, sql_data)  
    conn.commit()
    '''
    
    # ===== 자료 삭제 =====
    '''
    code = '14'
    # sql = "delete from sangdata where code=" + code # 권장 X
    # sql = "delete from sangdata where code='{0]'".format(code)
    
    sql = "delete from sangdata where code=%s" # 가장 많이 쓰임
    cursor.execute(sql, (code,)) # 매핑시 튜플 타입으로 주기
    conn.commit()
    '''
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
#         print(code, sang, su, dan)

    print()
    # 출력4
    for(a, b, c, d) in cursor:
        print(a, b, c, d)
except Exception as err:
    print(err)
    
finally:
    cursor.close()
    conn.close()
                                                                                                                                                                                                                            
