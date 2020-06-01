# 웹 문서를 읽어 형태소 분석

import urllib
from bs4 import BeautifulSoup
from konlpy.tag import Okt
from urllib import parse

okt = Okt()

# para = "이순신"
para = parse.quote("이순신")
# url = "https://ko.wikipedia.org/wiki/%EC%9D%B4%EC%88%9C%EC%8B%A0"
url = "https://ko.wikipedia.org/wiki/" + para
page = urllib.request.urlopen(url)
print(page)

soup = BeautifulSoup(page.read(), 'lxml')
# print(soup)

wordlist = []  # 명사들을 기억
for item in soup.select("#mw-content-text > div > p"):
    if item.string != None:
        # print(item.string.strip())
        ss = item.string
        wordlist += okt.nouns(ss)

print('wordlist : ', wordlist)
print('wordlist 단어수:' + str(len(wordlist)))

print()
wordDict = {}

for i in wordlist:
    if i in wordDict:
        wordDict[i] += 1
    else:
        wordDict[i] = 1
        
# 중복없이 단어보기
setData = set(wordlist)
print('중복없이 단어 보기 : ', setData)
print('중복없이 단어 수: ', len(setData))

print()
import pandas as pd

# 단어 뽑아낸거 확인
woList = pd.Series(wordlist)
print(woList[:3])
print(woList.value_counts()[:5])

# DataFrame에 저장
print()
df1 = pd.DataFrame(wordlist, columns=['단어'])
print(df1.head())
print()
df2 = pd.DataFrame([wordDict.keys(), wordDict.values()])
# print(df2)
df2 = df2.T
df2.columns = ['단어', '빈도수']
print(df2.head())

# file로 저장
df2.to_csv('이순신.csv', sep=',', index=False)

df3 = pd.read_csv('이순신.csv')
print(df3.head(3))

# 문) 홍길동전(완판본)을 읽은 후에 빈도수가 높은 10위 이내 단어 출력
