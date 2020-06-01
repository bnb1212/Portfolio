# 문) 홍길동전(완판본)을 읽은 후에 빈도수가 높은 10위 이내 2글자 이상의 단어 출력

import urllib
from bs4 import BeautifulSoup
from konlpy.tag import Okt
from urllib import parse

okt = Okt()

para = parse.quote("홍길동전_36장_완판본/현대어_해석")
url = "https://ko.wikisource.org/wiki/" + para

page = urllib.request.urlopen(url)

# print(page)

soup = BeautifulSoup(page.read(), 'lxml')

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

# count = 0
# for i in wordlist:
# #     print(i)
# #     if count > 10:
# #         break
#     if len(i) < 2:s
#         wordDict.pop(i, None)
    
#     if len(i) < 2:
#         del(wordDict[i])
        
import pandas as pd
import numpy as np
# DataFrame에 저장
print()
df1 = pd.DataFrame(wordlist, columns=['단어'])
# print(df1.head())
print()
        
df2 = pd.DataFrame([wordDict.keys(), wordDict.values()])
# print(df2)
df2 = df2.T
df2.columns = ['단어', '빈도수']
# print(df2.sort_values(by=['빈도수'], axis=0, ascending=False).head(10))

df3 = df2.sort_values(by=['빈도수'], axis=0, ascending=False)

# key에 접근할때는 str을 쓰자.
print(df3[(df3['단어'].str.len() >= 2)].to_string(index=False)).head()

# 빈도수 50 ~ 100 사이의 자료
df4 = df2[(df2['빈도수'] >= 50) & (df2['빈도수'] <= 100)]
print(df4)

# ndarray로 만들기
np4 = df4.values

print(type(np4))

# file로 저장
writer = pd.ExcelWriter('hong.xlsx', engine='xlsxwriter')
df3.to_excel(writer, sheet_name="Sheet1", index=False)
df2.to_excel(writer, sheet_name="Sheet2", index=False)
writer.save()
print('저장 성공')
# 
# exf = pd.ExcelFile('hong.xlsx')
# print(exf.sheet_names)

# DataFrame 반환함
# df3 = exf.parse("Sheet1")
