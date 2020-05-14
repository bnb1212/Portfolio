import cgi

# 사용자가 입력한 자료를 받음
form = cgi.FieldStorage()
irum = form['name'].value
nai = form['age'].value

print('Content-Type : text/html; charset=utf-8\n')
print('''
<html><body>
이름은 : {0}, 나이는 {1} <br>
<img src='../images/aaa.gif' width='1%' />
<br>
<a href="../main.html">메인으로 </a>
</body></html>

'''.format(irum, nai))



