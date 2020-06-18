'''=======================================
naive bayes 활용 비 예보 
======================================='''

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
from sklearn import metrics

# 데이터 읽어오기
df = pd.read_csv('../testdata/weather.csv')
# print(df.head(3))
# print(df.info())

# 독립변수
x = df[['MinTemp', 'MaxTemp', 'Rainfall', 'Cloud']]
# print(df['RainTomorrow'].unique()) # ['Yes' 'No']

# 종속 변수(Label)
label = df['RainTomorrow'].map({'Yes':1, 'No':0})

#print(label[:5])

# train / test 분리 : overfitting 방지
train_x, test_x, train_y, test_y = train_test_split(x, label, random_state = 0) 
# print(len(train_x), ' ', len(train_y))

# 모델 생성
gmodel = GaussianNB()
gmodel.fit(train_x, train_y)

# 예측(predict)
pred = gmodel.predict(test_x)
acc = sum(test_y == pred) / len(pred)
print("정확도 : ", acc)
print('정확도 : ', accuracy_score(test_y, pred))

# 분류 보고서
cl_report = metrics.classification_report(test_y, pred)

'''===
알고가기 - 정확도(Accuracy) : (TP + FN) / TOTAL 맞은걸 맞은걸로 예측 틀린걸 틀린걸로 예측
        민감도(Sensitivity): 실제 True인 것 중에서 모델이 True라고 예측한 것의 비율. 재현율(Recall)이라고도 한다. TP/TP+FP
        정밀도(Precision) : 모델이 True라고 분류한 것 중에서 실제 True의 비율. TP / TP+FN
        https://sumniya.tistory.com/26
==='''

# K-fold(K-교차검증) - 모델 학습시 입력자료를 k겹으로 나누어 학습과 검증을 함께하는 방법
from sklearn import model_selection
cross_val = model_selection.cross_val_score(gmodel, x, label, cv=5)
print(cross_val)
print(cross_val.mean())

print('새로운 자료로 예측 ---')
print(x.head(3))
import numpy as np
# MinTemp MaxTemp Rainfall Cloud
my_weather = np.array([[14.0, 26.9, 3.6, 3], [2.0, 11.9, 9.6, 30], [19.0, 30.9, 82.6, 90]])
print(gmodel.predict(my_weather))

            
             


