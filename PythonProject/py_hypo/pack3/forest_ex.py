'''==================================
중환자 치료실에 입원 치료받은 환자 200명의 생사여부에 관련된 자료다.
종속변수 STA에 영향을 주는 변수들을 찾아내어 검정 후에 해석하시오. 
예제 파일 : https://github.com/pykwon  ==>  patient.csv

<변수설명>
  STA : 환자생사여부
  AGE : 나이
  SEX : 성별
  RACE : 인종
  SER : 중환자 치료실에서 받은 치료
  CAN : 암 존재 여부
  INF : 중환자 치료실에서의 감염 여부
  CPR : 중환자 치료실 도착전 CPR여부
  HRA : 중환자 치료실에서의 심박수

kaggle.com이 제공하는 'wine quality' 분류 ( 0 - 10)
======================================='''
from sklearn.ensemble import RandomForestClassifier 
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 데이터 읽어오기
pt_data = pd.read_csv('../testdata/patient.csv')
print(pt_data.head())

# 결측치 제거
# print(pt_data.isnull().any()) # 결측치 하나도 없음

# 독립변수 / 종속변수 설정
#- 독립변수 ID를 제외한 나머지
x = pt_data.iloc[:, 2:]
# print(x)

#- 종속변수 
y = pt_data['STA']


# 데이터 분할 ( train / test )
train_x, test_x, train_y, test_y = train_test_split(x,y)

# 모델 생성
# n_estimators : 의사결정하는 트리 수
model = RandomForestClassifier(criterion='entropy', n_estimators=100, random_state=0)
model.fit(train_x, train_y)

pred = model.predict(test_x)

print('예측값 : ', pred[:5])
print('실제값 : ', np.array(test_y[:5]))

# 분류 정확도
from sklearn.metrics import accuracy_score
print('분류 정확도 : ', accuracy_score(test_y, pred))

print('특성 중요도 :\n{}'.format(model.feature_importances_))

# 특성 중요도 시각화
def plot_feature_importances(model):
    n_features = x.shape[1]
    # 바차트(horizon)
    plt.barh(range(n_features), model.feature_importances_, align='center')
    plt.yticks(np.arange(n_features), x.columns)
    plt.xlabel("attr importances")
    plt.ylabel("attr")
    plt.ylim(-1, n_features)
    plt.show()
    plt.close()
    
plot_feature_importances(model)

print('\n----------------------------------------------------------\n')
wine_data = pd.read_csv("../testdata/winequality-red.csv")
# print(wine_data.head(3))

# 결측치 제거
# print(wine_data.isnull().any()) # 결측치 하나도 없음

# 독립변수 / 종속변수 설정
#- 독립변수 ID를 제외한 나머지
x = wine_data.iloc[:, 0:-1]
# print(x)

#- 종속변수 
y = wine_data['quality']

# 데이터 분할 ( train / test )
train_x, test_x, train_y, test_y = train_test_split(x,y)

# 모델 생성
# n_estimators : 의사결정하는 트리 수
model = RandomForestClassifier(criterion='entropy', n_estimators=500, random_state=0)
model.fit(train_x, train_y)

pred = model.predict(test_x)

print('예측값 : ', pred[:5])
print('실제값 : ', np.array(test_y[:5]))

# 분류 정확도
from sklearn.metrics import accuracy_score
print('분류 정확도 : ', accuracy_score(test_y, pred))
print('특성 중요도 :\n{}'.format(model.feature_importances_))

plot_feature_importances(model)