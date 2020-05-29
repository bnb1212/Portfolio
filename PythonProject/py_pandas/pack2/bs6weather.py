import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
import pandas as pd

url = "http://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp"
data = urllib.request.urlopen(url).read()

# 인코딩이 되어있음
# print(data.decode('utf-8'))

soup = BeautifulSoup(data, 'lxml')
# print(soup)

title = soup.find('title').string
print(title)

# CDATA 는 XML 에서 파싱하지 않은 문자데이터 를 의미한다.

print(soup.find('wf'))
city = soup.find_all('city')
print(city)

cityDatas = []

for c in city:
    #print(c.string)
    cityDatas.append(c.string)
    
df = pd.DataFrame()
df['city'] = cityDatas
# print(df.head(3))

# tmEf = soup.select_one('location > data > tmef')
# tmEf = soup.select_one('location data tmef')

# 직계 자식 >, 형재 +
tmEf = soup.select_one('location > province + city + data > tmef')
print(tmEf)

tempMins = soup.select('location > province + city + data > tmn')
tempDatas = []

for t in tempMins:
    print(t.string)
    tempDatas.append(t.string)
    
df['temp_min'] = tempDatas
df.columns = ['지역', '최저기온']
print(df.head(3))
print(df[0:3])

print(df.tail(3))
print(df[-3:len(df)])
# 파일로 저장
# df.to_csv('날씨.csv', index = False)

print()
print('iloc, loc --------------------------------------------------------\n')
# 하나 일땐 Series
print(print(df.iloc[0], type(df.iloc[0])))
print()
# 복수개 일떈 Dataframe으로 슬라이싱됨
print(print(df.iloc[0:2], type(df.iloc[0:2])))
print(print(df.iloc[0:2, :], type(df.iloc[0:2, :])))
print()
print(df.iloc[0:2, 0:1])
print(df.iloc[0:2, 0:2])
print()
print(df['지역'][0:2], type(df['지역'][0:2]))
print(df['지역'][:2])
print(df.지역[:2])
# print(df[:])  == print(df)


print('\n---------------------------------------------------------------------\n')


print(df.loc[1:3]) # print(df.loc['a':'c'])
print(df[1:4])
print(df.loc[[1,3]])
print(df.loc[:, '지역'])

print()
print(df.loc[1:3, ['최저기온', '지역']])
print(df.loc[:,'지역'][1:4])

print('\n--------------------------------------------------------------------\n')

print(df.info())
# 타입 변경
df = df.astype({'최저기온':int})
print(df.info())
print(df['최저기온'].mean())
print(df['최저기온'].describe())
print()
print(df['최저기온'] >= 19)
# 조건걸어 검색
print(df.loc[df['최저기온'] >= 19])
print(df.loc[(df['최저기온'] >= 18) & (df['최저기온'] < 20)]) # and : & or : |
print(df.loc[df['최저기온'] >= 19, ['최저기온']][0:3])
print()
print(df.sort_values(['최저기온'], ascending=True))

