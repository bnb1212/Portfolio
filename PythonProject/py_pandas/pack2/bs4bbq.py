# BBQ 사이트 자료 읽고 메뉴와 가격 출력. 가격 평균, 표준 편차
import urllib.request as req
import bs4

bbqurl = "https://www.bbq.co.kr/menu/menulist.asp"
bbq = req.urlopen(bbqurl)
print(bbq)

soup = bs4.BeautifulSoup(bbq, 'lxml')
# 메뉴명
data1 = soup.select('div.box > div.info > p.name')
# 가격 
data2 = soup.select('div.box > div.info > p.pay')

name = []
pay = []

for a in data1:
    name.append(a.text)
    
print(name)

for b in data2:
    pay.append(int(b.text.replace(',', '').replace('원', '')))
    
print(pay)

data = {'name':name, 'pay':pay}
from pandas import DataFrame
df = DataFrame(data)
print(df)

print('-----------------------------------------------------')
soup = bs4.BeautifulSoup(bbq, 'lxml')
datas = []
info = soup.select('div.info')


        


