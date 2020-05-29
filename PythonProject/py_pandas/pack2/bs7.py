# 웹 문서 일부 읽고 파일로 저장
from bs4 import BeautifulSoup
import urllib.request as req
import datetime

url = "https://finance.naver.com/marketindex/"
data = req.urlopen(url)
print(data)
soup = BeautifulSoup(data, 'html.parser')

price = soup.select_one('div.head_info > span.value').string
print('미국USD', price)

# 스케쥴러를 만들어 일정시간마다 읽어올 수 있다.
# t = datetime.date.today()
t = datetime.datetime.now()
print(t)
fname = t.strftime('%Y-%m-%d-%H-%M-%S') + '.txt'
print(fname)

with open(fname, 'w', encoding='utf-8') as f:
    f.write(price)

