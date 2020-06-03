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

# 빈도수 높은 단어 확인
print(Counter(words_basket).most_common(50))    

movies = [m.replace('ㅋㅋㅋㅋ','') for m in movies]
movies = [ m.replace('저런','') for m in movies]
movies = [ m.replace('있었고','') for m in movies]
print(movies, len(movies))
print('--------------------------------------------------------------------------')
def word_separate(movises):
    result = []
    for mov in movies:
        words = okt.pos(mov)
        one_result = []
        for word in words:
            if(word[1] in ['Noun', "Adjective"]) and len(word[0]) >= 2:
                one_result.append(word[0])
        result.append(" ".join(one_result))
    return result

word_list= word_separate(movies)
print(word_list)
print(len(word_list))
print()
print('---------------------------------------------------------------------------------------')
# 토큰 생성 후 벡터화
# 1 : CountVectorizer()
count = CountVectorizer(min_df=2)
print(count)
cou_dtm = count.fit_transform(word_list).toarray()
print(cou_dtm)
cou_dtm_df = pd.DataFrame(cou_dtm, columns = count.get_feature_names(),
                          index = ['yeogoksung', 'rpoint', 'nalci', 'goyang2', 'coco'])
print(cou_dtm_df)


print('---------------------------------------------------------------------------------------')
# 2 : TfidfVectorizer()
idf_maker = TfidfVectorizer(min_df = 2)
tfidf_dtm = idf_maker.fit_transform(word_list).toarray()
print(tfidf_dtm)
tfidf_dtm_df = pd.DataFrame(tfidf_dtm, columns=count.get_feature_names(),
                            index = ['yeogoksung', 'rpoint', 'nalci', 'goyang2', 'coco'])
# 단어들의 중요도를 알 수 있는 가중치로 출력
print(tfidf_dtm_df)

# 코사인 유사도를 이용해 단어의 유사성 출력
def cosin_func(doc1, doc2):
    bunja = sum(doc1 * doc2)
#     bunmo = ((sum(doc1) ** 2) * (sum(doc2) ** 2)) ** 0.5
#     bunmo = ((sum(doc1 ** 2)) ** 0.5) * ((sum(doc2 ** 2)) ** 0.5)
    bunmo = (sum(doc1 ** 2) * sum(doc2 ** 2)) ** 0.5
    return bunja /bunmo

res = np.zeros((5, 5))
print(res)

for i in range(5):
    for j in range(5):
        res[i, j] = cosin_func(tfidf_dtm_df.iloc[i], tfidf_dtm_df.iloc[j].values)

df = pd.DataFrame(res, index = ['yeogoksung', 'rpoint', 'nalci', 'goyang2', 'coco'],
                  columns= ['yeogoksung', 'rpoint', 'nalci', 'goyang2', 'coco'])

print(df)



