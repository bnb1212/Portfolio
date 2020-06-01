# 신문사 사이트에서 검색 단어 입력후 해당 단어 기사들 정보 읽어 워드 클라우드 출력
from bs4 import BeautifulSoup
import urllib.request
from urllib.parse import quote

# keyword = input('검색어 입력 : ')
keyword = "코로나"

print(quote(keyword))

# 신문사 url
targeturl = "https://www.donga.com/news/search?query=" + quote(keyword)
print(targeturl)
searchData = urllib.request.urlopen(targeturl)
soup = BeautifulSoup(searchData, 'lxml', from_encoding='utf-8')

# print(soup)
msg = ""
for title in soup.find_all("p", 'tit'):  # p태그 중에서 속성이 tit인 놈
    title_link = title.select('a')
#     print(title_link)
    article_url = title_link[0]['href']
    print(article_url)
    
    source_article = urllib.request.urlopen(article_url) # 각 a tag의 기사 내용 읽기
    soup = BeautifulSoup(source_article, 'lxml', from_encoding='utf-8')
    contents = soup.select('div.article_txt')
    
    for imsi in contents:
        item = str(imsi.find_all(text=True))
#         print(item)
        msg = msg + item
        
print(msg)

print()    
from konlpy.tag import Okt
from collections import Counter

nlp = Okt()
# 명사별로 분할
nouns = nlp.nouns(msg) 
result = []
for imsi in nouns:
    if len(imsi) > 1:
        result.append(imsi)
        
print(result[:10])

count = Counter(result)
# tag = print(count) # Counter({'판매': 50, '코로나': 44, '추가': 26, '모델': 24, ...
tag = count.most_common(50)

import pytagcloud

taglist = pytagcloud.make_tags(tag, maxsize=100)
print(taglist[:5])
pytagcloud.create_tag_image(taglist, "morph4word.png", size=(1000, 600), fontname='Nobile', rectangular=False)

# 저장된 이미지 읽기
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# 한글 이미지가 깨져서 나온다.
# Lib - sitepakages 에 한글 글꼴을 넣어 주어야 한다.
# 적당한 한글 폰트를 복사해 pytagcloud 폴더에 넣어주자.
# fonts.json파일을 수정해야한다.
img = mpimg.imread("morph4word.png")
plt.imshow(img)
plt.show()

# 브라우저로 출력
import webbrowser
webbrowser.open('morph4word.png')


