# file 읽기
import pandas as pd

# csv 파일 읽기
df = pd.read_csv("../testdata/ex1.csv")
print(df, type(df))
print()

# csv를 테이블로 읽기 ( 구분자 sep을 인자로 준다 )
df = pd.read_table("../testdata/ex1.csv", sep=',')
print(df)
print()

# 헤더 없음 
df = pd.read_csv("../testdata/ex2.csv", header=None)
print(df)
print()

# 헤더 없고 헤더 이름 주기
# df = pd.read_csv("../testdata/ex2.csv", header=None, names=['a', 'b'])
df = pd.read_csv("../testdata/ex2.csv", header=None, names=['a', 'b', 'c', 'd', 'e'])
print(df)
print()

# 인덱스 컬럼 할당
df = pd.read_csv("../testdata/ex2.csv", header=None, names=['a', 'b', 'c', 'd', 'e'], index_col='e')
print(df)
print()

# txt 파일 읽기
df = pd.read_table("../testdata/ex3.txt")
print(df)
print()

# txt지만 csv로 읽어도 읽어지긴 함
df = pd.read_csv("../testdata/ex3.txt")
print(df)
print()

# 1행 3행 빼기
df = pd.read_csv("../testdata/ex3.txt", sep='\s+', skiprows=[1, 3])  # skiprows는 튜플형태로 써도 됨
print(df)
print()

# 구분자 없이 붙어있는 애들 글자수로 나눔(widths)
df2 = pd.read_fwf('../testdata/data_fwt.txt', widths=(10, 3, 5), encoding='utf-8', names=('날짜', '기업명', '가격'))
print(df2)

# chunk : 대용량의 파일인 경우에는 원하는 크기만큼 할당해서 읽을 수 있다. (막 레코드 백만개짜리 같은거)
datas = pd.read_csv('../testdata/data_csv2.csv', header=None, chunksize=3)
# <pandas.io.parsers.TextFileReader object at 0x000001D4FB08CBC8>
print(datas)
for p in datas:
    #print(p)
    print(p.sort_values(by=2, ascending=True))

