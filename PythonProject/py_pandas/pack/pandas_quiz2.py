#  df = pd.read_csv('파일명',  header=None,,,)  
# 
#  1) 성별, 선실(class or pclass), 나이대(소년, 청년, 장년, 노년)에 의한 생존율을 데이터프레임을 사용해 계산한다.
#      행에는 성별 및 나이에 대한 계층적 인덱스(pd.cut())를 사용하고, 열에는 선실 인덱스를 사용한다.
import pandas as pd
import numpy as np

print("------------------ Quiz 3 -----------------------------")
df = pd.read_csv('../testdata/titanic_data.csv', index_col=['PassengerId'])
print(df)
# print(df.T)
# print(df.pivot_table(values=['pop'], index=['year'], columns=['city'], margins=True, fill_value=0))
# df_1 = df.pivot_table(index=['Sex', 'Age'], columns=['Pclass'])
# print(df_1)

bins = [1, 20, 35, 60, 150]
labels = ["소년", "청년", "장년", "노년"]
df["age_cat"] = pd.cut(df['Age'], bins, labels=labels)
print(df)

print(" ---------------------------------------------------------성별 / 나잇대 / 선실별 생존율 ----- ")
print(df.pivot_table(values=['Survived'], index=['Sex','age_cat'], columns=['Pclass'], aggfunc=np.mean, fill_value=0))

test_df = df.groupby([df['Sex'],df['age_cat'],df['Pclass']])['Survived'].mean()
print("테스트")
print(type(test_df))
print(test_df)
print(" ---- 피벗 테이블 ----")
print(df.pivot_table(values=['Survived'], index=['Sex'], columns=['Pclass'], aggfunc=np.mean))

print("------------------- Quiz 4 ------------------------------")
# 각 컬럼명 / values에 공백이 있음
# df2 = pd.read_csv('../testdata/human.csv', na_values=' NA')
# df2.rename(columns=lambda x: x.strip())
# print(df2)
try:
    print('-------- NA 삭제 ------')
    df2 = pd.read_csv('../testdata/human.csv', skipinitialspace=True)
    print(df2.dropna())
    print()
    print('-------- 칼럼 추출하여 DF 작성 ------')
    p_df2 = df2.loc[:,['Career', 'Score']]
    print(p_df2)
    print("Career 평균 :",p_df2['Career'].mean())
    print("Score 평균 :",p_df2['Score'].mean())
except Exception as e:
    print("Error : " + str(e))


print("----------------------------------------------------------")
#  2) tips.csv 파일을 읽어 아래와 같이 처리하시오.
#      - 파일 정보 확인
#      - 앞에서 3개의 행만 출력
#      - 요약 통계량 보기
#      - 흡연자, 비흡연자 수를 계산  : value_count()
#      - 요일을 가진 칼럼의 유일한 값 출력  : unique()
try:
    df3 = pd.read_csv('../testdata/tips.csv')
    print("----파일정보 확인 -----")
    print(df3)
    print()
    print("---- 앞에서 3개행 ----")
    print(df3.head(3))
    print()
    print("---- 요약 통계량 ----")
    print(df3.describe())
    print()
    print("---- 흡연자, 비흡연자 수 계산 ----")
    print(df3['smoker'].value_counts())
    print("---- 요일 칼럼 유일한 값 출력 ----")
    print(df3['day'].unique())
except Exception as e:
    print("Error : " + str(e))
    
# 데이터 읽기 기본적 순서
# 파일 읽기 -> shape/head 확인 -> columns 확인 -> 필요한 열 뽑아낸 df만들기
# head / tail 확인 -> 각 열의 데이터타입 눈 확인 -> 문자열 데이터 범주 확인
# 결측값(NaN) 제거 후 shape 확인 