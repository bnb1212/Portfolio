import cgi

form = cgi.FieldStorage()  # ('name':'tom'...)
name = form['name'].value
phone = form['phone'].value
gen = form['gen'].value

print('Content-Type : text/html; charset=utf-8\n')
print('''
<html><body>
이름은 : {0}, 전화는 {1}, 성별은 {2} <br>
<br>
<a href="../main.html">메인으로 </a>
</body></html>

'''.format(name, phone, gen))
