# naver의 영화 순위 읽기
# 방법 1
import urllib.request
from bs4 import BeautifulSoup
url = "https://movie.naver.com/movie/sdb/rank/rmovie.nhn"
data = urllib.request.urlopen(url).read()
soup = BeautifulSoup(data, 'lxml')
# print(soup)
# print(soup.select('div.tit3'))
# print(soup.select('div[class=tit3]'))

for tag in soup.select('div[class=tit3]'):
    print(tag.text.strip())

# 방법 2
import requests

# data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn')
# print(data.status_code, ' ', data.encoding)
# datas = data.text
# print(datas)

datas = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn').text
soup = BeautifulSoup(datas, 'lxml')
print(soup)
m_list = soup.findAll('div', 'tit3')
m_list = soup.findAll('div', {'class':'tit3'})
# print(m_list) # <a href="/movie/bi/mi/basic.nhn?code=193992" title="런 보이 런">런 보이 런</a>

# 참고해보기
title = 'abcdefg'
print(title[title.find('b'):title.find('f')]) # bcde

for i in m_list:
#     print(i)
    title = i.findAll('a')
#     print(str(title))[7:10]
    print(str(title)[str(title).find('title="')+7:str(title).find('">')])
    
print('\n순위 표시---------------------------------------------------------------\n')
count = 1
for i in m_list:
    title = i.find('a')
    print(str(count) + '위:' + title.string)
    count += 1
    
    




