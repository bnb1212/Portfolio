'''======================================================
[XGBoost 문제] 
kaggle.com이 제공하는 'glass datasets'
유리 식별 데이터베이스로 여러 가지 특징들에 의해 7가지의 label(Type)로 분리된다.

RI    Na    Mg    Al    Si    K    Ca    Ba    Fe    
 Type
                          ...

glass.csv 파일을 읽어 분류 작업을 수행하시오.
======================================================'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import xgboost as xgb

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
import random

# 데이터 읽어오기
data = pd.read_csv('../testdata/glass.csv')
# print(data.info())

# 결측치 체크
# print(data.isnull().any()) #없음

# 변수설정
feature = data.iloc[:, :-1]
label = data['Type']
# print(feature.info())
# print(label)

# 테스트 데이터 30%
x_train, x_test, y_train, y_test = train_test_split(feature, label, test_size=0.3)

# 학습 진행

model = xgb.XGBClassifier(booster='gbtree',  # XGBClassifier
                max_depth=4,
                n_estimators=1000) 

model.fit(x_train, y_train)

# 예측
y_pred = model.predict(x_test)
print('예측값 : ', y_pred[:5])
print('실제값 : ', np.array(y_test[:5]))
print('정확도 : ', metrics.accuracy_score(y_test, y_pred))

# 새 랜덤값 넣어보기
feature_rand = [[]]
for i in range(feature.shape[1]):
    feature_rand[0].append(random.uniform(data.iloc[:, i].min(), data.iloc[:, i].max()))

print(feature_rand)
feature_rand = pd.DataFrame(feature_rand, columns=['RI', 'Na', 'Mg', 'Al', 'Si', 'K', 'Ca', 'Ba', 'Fe'])
y_pred = model.predict(feature_rand)
print('랜덤 값 예측 : ', y_pred)
