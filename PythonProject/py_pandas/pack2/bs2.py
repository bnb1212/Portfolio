# HTML / XML 전용 처리 모듈 : Beautiful Soup 
from bs4 import BeautifulSoup

html_data = """
<html>
    <body>
        <h1>Bravo ! my Life</h1>
        <p>웹 페이지 분석</p>
        <p>원하는 자료를 얻어보자!</p>
    </body>
</html>
"""

print(html_data, type(html_data))

soup = BeautifulSoup(html_data, 'html.parser')
print(soup, type(soup))

h1 = soup.html.body.h1
# 같은 태그가 여러개일때
p1 = soup.html.body.p
p2 = p1.next_sibling.next_sibling
print(h1, ' ', h1.string)
print(p1, ' ', p1.string)
print(p2, ' ', p2.string)

print('------------------------------------------')
# id 넣어보기
html_data2 = """
<html>
    <body>
        <h1 id='title'>Bravo ! my Life</h1>
        <p>웹 페이지 분석</p>
        <p id='my'>원하는 자료를 얻어보자!</p>
    </body>
</html>
"""
soup2 = BeautifulSoup(html_data2, 'lxml')
# print(soup2)
print(soup2.p)
print(soup2.p.string)
# find 사용
print(soup2.find('p'), soup2.find('p').string)
print(soup2.find('p', id='my'), soup2.find('p', id='my').string)
print(soup2.find(id='title').string)
print(soup2.find(id='my').string)

print('-------------------------------------------')
html_data3 = """
<html>
    <body>
        <h1 id='title'>Bravo ! my Life</h1>
        <p>웹 페이지 분석</p>
        <p id='my'>원하는 자료를 얻어보자!</p>
        <div>
            <a href='http://www.naver.com'>naver</a>
            <a href='http://www.daum.net'>daum</a>
        </div>
    </body>
</html>
"""

soup3 = BeautifulSoup(html_data3, 'lxml')
print(soup3)
print(soup3.find('a'))
print(soup3.find('a').string)
print(soup3.find(['a']))

# find_all 하면 list로 반환하게 됨
print(soup3.find_all('a'))
# print(soup3.find_all(['a'])) 
# print(soup3.findAll(['a']))

links = soup3.find_all('a')
print(links)

for i in links:
    href = i.attrs['href']
    text = i.string
    print(href, ' ', text)
    
print(soup3.find_all('p'))

# element 여러개 찾기
print(soup3.find_all(['p', 'h1']))

# string으로 조건 주면서 찾기(search)
aa = soup3.find_all(string=['원하는 자료 추출', '웹 페이지 분석', 'Bravo ! my Life'])
print(aa)

#정규표현식으로 찾기
print('정규 표현식 가능')
import re
links2 = soup3.find_all(href=re.compile(r'^ht'))
print(links2)
for h in links2:
    print(h.attrs['href'])
    
print('\n\nCSS Selector ------------------------------------------')
html_data4 = """
<html>
<body>
<div id='hello'>
    <a href='http://www.naver.com'>naver</a>
    <span>
        <i>
            <a href='http://www.asia.com'>asia</a>
        </i>
        <a href='http://www.korea.com'>korea</a>        
    </span>
    <ul class='world'>
        <li>얀녕</li>
        <li>뱐가워</li>
    </ul>
    <ul class='kbs'>
        <li>goods</li>
        <li>nice</li>
    </ul>    
</div>
<div id='sbs'>
    <b>나는 Bold</b>
    <a href='http://www.mbc.com'>mbc</a>
</div>
</body>
</html>
"""
soup4 = BeautifulSoup(html_data4, 'lxml')
# a = soup4.select_one('div a')
a = soup4.select_one('div#sbs a')
print('a :',a)

b = soup4.select_one('div#hello a').string
print('b :',b)
# 직계 자식은 >
c = soup4.select_one('div#hello span > a').string
print('c :',c)

d = soup4.select_one('div#hello span a').string
print('d :',d)

e = soup4.select('div#hello ul.world > li')
print('e :',e)

for abc in e:
    print(abc.string)
