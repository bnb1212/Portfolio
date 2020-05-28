# BBQ 사이트 자료 읽고 메뉴와 가격 출력. 가격 평균, 표준 편차
import urllib.request as req
import bs4

bobae_url = "https://www.bobaedream.co.kr/mycar/mycar_list.php?gubun=K"
bobae_url = req.urlopen(bobae_url)
print(bobae_url)

soup = bs4.BeautifulSoup(bobae_url, 'lxml')
# 메뉴명
test_data = soup.select("#listCont > div.wrap-thumb-list > ul > li > div")
print(test_data)
data1 = soup.select('#listCont > div.wrap-thumb-list > ul > li > div > div.mode-cell.title > p.tit')
# print(data1)
# 가격 
data2 = soup.select('#listCont > div.wrap-thumb-list > ul > li > div > div.mode-cell.price > b > em')

name = []
pay = []

for a in data1:
    name.append(a.text.replace('\n', ''))
    
print(name)

for b in data2:
    pay.append(int(b.text.replace(',','')))
    
print(pay)

data = {'name':name, 'price':pay}
from pandas import DataFrame
print(len(data['name']))
print(len(data['price']))
df = DataFrame(data)
print(df)
print('평균 :',df['price'].mean())
print('표준편차 :',df['price'].std())

