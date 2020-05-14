import cgi
import MySQLdb

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
    cursor = conn.cursor()
    cursor.execute("select * from sangdata")
    
    print('Content-Type : text/html; charset=utf-8\n')
    
    print('<html><body> * 상품 자료 * <br>')
    print('<table border="1">')
    print('<tr><th>코드</th><th>품명</th><th>수량</th><th>단가</th></tr>')
    datas = cursor.fetchall()
    for d in datas:
        print('''
            <tr>
                <td>{0}</td>
                <td>{1}</td>
                <td>{2}</td>
                <td>{3}</td>
            </tr>        
        '''.format(str(d[0]), str(d[1]), str(d[2]), str(d[3])))

    print('</table></body></html>')
except Exception as err:
    print("err : " + err)
    
finally:
    cursor.close()
    conn.close()
