# naver 영화 네티즌 평점 자료로 영화간 유사도 출력

from bs4 import BeautifulSoup
import requests
from konlpy.tag import Okt
from collections import Counter
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer  


def movie_scrap(url):
    result = []
    # 1 ~ 10페이지 읽기
    for p in range(10): 
        r = requests.get(url + "&page=" + str(p))
        soup = BeautifulSoup(r.content, 'lxml', from_encoding='ms949')
        
#         print(soup)
        title = soup.find_all("td", {"class":"title"})
#         print(title)
        sub_result = []
        for i in range(len(title)):
            # 별점 외에 다른 것들 지우면서 추가
            sub_result.append(title[i].text
                              .replace('\r', '')
                              .replace('\t', '')
                              .replace('\n', '')
                              .replace('신고', '')
                              .replace('-', '')
                              .replace(',', '')
                              .replace('.', '')
                              .replace('...', '')
                              .replace('여곡성', '')
                              .replace('고양이의 보은', '')
                              .replace('날씨의 아이', '')
                              .replace('알포인트', '')
                              .replace('코코', '')
                              .replace('영화', '')
                              )
        result = result + sub_result

    return("".join(result))
        
        
yeogoksung = movie_scrap("https://movie.naver.com/movie/point/af/list.nhn?st=mcode&sword=171750&target=after")
rpoint = movie_scrap("https://movie.naver.com/movie/point/af/list.nhn?st=mcode&sword=37261&target=after")
nalci = movie_scrap("https://movie.naver.com/movie/point/af/list.nhn?st=mcode&sword=181114&target=after")
goyang2 = movie_scrap("https://movie.naver.com/movie/point/af/list.nhn?st=mcode&sword=37073&target=after")
coco = movie_scrap("https://movie.naver.com/movie/point/af/list.nhn?st=mcode&sword=151728&target=after")

movies = [yeogoksung, rpoint, nalci, goyang2, coco]
print(movies)

# 단어 빈도 수
words_basket = []
okt = Okt() 
for mov in movies:
    words = okt.pos(mov)
    for word in words:
        if(word[1] in ['Noun', 'Adjective'] and len(word[0]) >= 2):
            words_basket.append(word[0])

print(words_basket)
print(Counter(words_basket).most_common(50))    
