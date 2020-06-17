'''=============================================
Heart 데이터는 흉부외과 환자 303명을 관찰한 데이터다. 
각 환자의 나이, 성별, 검진 정보 컬럼 13개와 마지막 AHD 칼럼에 각 환자들이 심장병이 있는지 여부가 기록되어 있다. 
데이터셋을 학습을 위한 train 셋과 test셋으로 구분하고 분류 모델을 만들어 모델 객체를 호출할 경우 정확한 확률을 확인하시오. 
임의의 값을 넣어 분류결과를 확인하시오. 정확도가 예상보다 적게 나올 수 있음에 실망하지 말자. ㅎㅎ

feature 칼럼 : 문자 데이터 칼럼은 제외
label 칼럼 : AHD
==============================================='''
import random 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection._split import train_test_split
from sklearn import svm, metrics
from sklearn.preprocessing._data import StandardScaler

random.seed(124)

data = pd.read_csv('../testdata/heart.csv')
print(data)

# AHD 칼럼 Yes, No를 1, 0으로 매핑
data['AHD']=data['AHD'].map({'Yes':1, 'No':0})

# 문자데이터 칼럼 제외(0: 번호, unnamed / 3 : ChestPain / 13 : Thal)
# print(data.iloc[1,:])
data = data.drop(data.columns[[0, 3, 13]], axis='columns')
data = data.dropna()
print(data)

# feature(독립변수)
feature = np.array(data.iloc[:, 0:-1])
print(feature)

# label(종속변수)
label = np.array(data.iloc[:, -1:])
# print(label)

# train / test dataset 분리(split)
data_train, data_test, label_train, label_test = train_test_split(feature, label)

# 스케일링 (데이크 크기 표준화)
# StandardScaler() 평균이 0, 표준편차가 1이되도록 변환해준다.  
# 참고 - 정규화 : MinMaxScaler()
sc = StandardScaler()
print(sc)
sc.fit(data_train)
sc.fit(data_test)
x_train = sc.transform(data_train)
x_test = sc.transform(data_test)
print('\n스케일링 처리 후')
print(x_train[:3])


# 모델 학습
model = svm.SVC(C=10).fit(data_train, label_train.ravel()) 
# ravel()메소드는 다차원 배열을 평평하게 1차원배열로 만들어준다 (경고제거)
# DataConversionWarning: A column-vector y was passed when a 1d array was expected.
print(label_train.ravel())  
pred = model.predict(data_test)
print('실제값: ', pred[:3])
print('예측값: ', label_test[:3])

# K-겹 교차검증 : Overfitting 방지용
from sklearn import model_selection
cross_vali = model_selection.cross_val_score(model, data_train, label_train.squeeze(), cv=5) 
print('각각(5겹)의 검증 정확도: ',cross_vali)
print('평균(5겹)의 검증 정확도: ',cross_vali.mean())

# 분류 정확도 확인
ac_score = metrics.accuracy_score(label_test, pred)
print('정확도: ', ac_score) # 약 0.5867 
# print('Support Vector Value :',model.support_vectors_)
 
# 임의의 값 넣어 테스트
feature_rand = [[]]
for i in range(0, 11):
    feature_rand[0].append(random.uniform(data.iloc[:,i].min(), data.iloc[:,i].max()))

# print(data.sample(n=1))
# print(data['Chol'].max())
print('랜덤 생성 :',feature_rand)
pred = model.predict(feature_rand)
print("예측값 :", pred)

