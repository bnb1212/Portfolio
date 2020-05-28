import urllib.request as req
import bs4
from pandas import DataFrame

maserati_url = 'https://www.bobaedream.co.kr/mycar/mycar_list.php?gubun=I&maker_no=18&page=1&order=S11&view_size=20'
maserati = req.urlopen(maserati_url)
maserati_soup = bs4.BeautifulSoup(maserati,'lxml')
maserati_name = maserati_soup.select('p.tit > a') # 차 이름 가져오기
maserati_advice = maserati_soup.select('div.mode-cell.price > b') # 가격이 '상담'인 아이들
maserati_value = maserati_soup.select('div.mode-cell.price > b > em') #가격이 숫자인 아이들


count = 0
maserati_nickname = []
maserati_price = []

# list에 이름 넣어주기
for name in maserati_name:
    maserati_nickname.append(name.string)


# list에 가격 채워주기
for a in maserati_advice:

    if a.string == '상담':
        maserati_price.append(a.string)
    else:
        # 상담이 아닌 자리에 가격을 넣은 후 가격의 ,를 빼고 정수형으로 형변환
        maserati_price.append(int(maserati_value[count].string.replace(',','')))
        count = count+1

# 빈 dataframe 생성
df_datas = DataFrame(index=range(0,len(maserati_nickname)), columns=['이름', '가격'])

# 칼럼에 정보를 넣기
df_datas['이름'] = maserati_nickname
df_datas['가격'] = maserati_price

# 원래 데이터
print('\n---------------- Raw Data ----------------\n')
print(df_datas)
df_datas = df_datas[df_datas['가격'] !='상담']

# 가공후
print('\n----------------Information ----------------\n')
print(df_datas)

# 평균과 표준편차
print('\n---------------- Average & STD ----------------\n')
print('가격평균:',df_datas['가격'].mean(),'만원')
print('가격표준편차:',df_datas['가격'].std())
