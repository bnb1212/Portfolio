# 위키 백과 자료 읽기
import urllib.request as req
from bs4 import BeautifulSoup

url = "https://ko.wikipedia.org/wiki/%EC%9D%B4%EC%88%9C%EC%8B%A0"
wiki = req.urlopen(url)
soup = BeautifulSoup(wiki, 'lxml')
# print(soup)

# 개발자도구 copy selector
# #mw-content-text > div > p:nth-child(6)
print(soup.select_one("#mw-content-text > div > p"))

print('---------------------------------------------------------')
daumurl = "https://news.v.daum.net/v/20200528120811852"
daum = req.urlopen(daumurl)
print(daum)

soup = BeautifulSoup(daum, 'lxml')
# print(soup)
print(soup.select_one('div#kakaoIndex > a').string)
datas= soup.select('div#kakaoIndex > a')
# print(datas)
for i in datas:
#     print(i)
    href= i.attrs['href']
    text = i.string
    print('href : {}, text :{}'.format(href, text))
    

print()
datas2 = soup.find_all('a')
print(datas2)

for i in datas2[:2]:
    print(i)
    text = i.string
    print(text)

print()
print('------------------------------------------------------------')
# #harmonyContainer > section > p:nth-child(5)
datas3 = soup.select("#harmonyContainer > section > p")
for i in datas3[2:3]:
    print(i.string)

