# 교차 테이블 작성 : 행과 열로 구성되는 교차표. 변수들 간에 유의미한 차이 파악이 용잏다.
import pandas as pd

ytrue = pd.Series([2, 0, 2, 2, 0, 1, 1, 2, 0])
ypred = pd.Series([2, 1, 1, 2, 0, 1, 0, 1, 0])

# 크로스탭에 들어오는 데이터는 범주형 데이터가 되어야 한다.
kbs = pd.crosstab(ytrue, ypred, rownames = ['True'], colnames=['pred'], margins=True)
print(kbs)

print('예측 정확도 :',(2+1+2)/9)

print('-------------------------------------------------')
des = pd.read_csv('../testdata/descriptive.csv')
print(des.info())
print(des.head(3))

# 명목 척도 / 순서 척도 - 범주형
# 간격 척도 / 비율 척도 - 연속형
# 컬럼의 형을 파악해야함

data = des[['resident', 'gender', 'level', 'pass']]
print(data[:3], type(data))

table = pd.crosstab(data.resident, data.gender)
print(table)
table2 = pd.crosstab([data.resident, data.gender], data.level)
print(table2)