'''========================================================
RandomForest 분류분석 : 여러 개의 DecisionTree를 조합(ensemble)
======================================================='''
from sklearn.ensemble import RandomForestClassifier 
from sklearn.model_selection import train_test_split
import pandas as pd

df = pd.read_csv("../testdata/titanic_data.csv")
print(df.shape)

# null값이 컬럼에 있는지 확인할 수 있다 isnull().any()
print(df.isnull().any())
df = df.dropna(subset=['Embarked', 'Cabin', 'Age'])
df_x = df[['Pclass', 'Age', 'Sex']]
print(df_x.head(3))

# Scaling(스케일링)
from sklearn.preprocessing import OneHotEncoder, LabelEncoder
df_x.loc[:, 'Sex'] = LabelEncoder().fit_transform(df_x['Sex']) # female : 0, male : 1
print(df_x.head(3))
df_y = df['Survived']
print(df_y.head(3))

# Pclass를 first.class, second.class, third.class

import numpy as np
df_x2 = pd.DataFrame(
                    OneHotEncoder().fit_transform(df_x['Pclass'].values[:, np.newaxis]).toarray(),\
                     columns=['f_cls','s_cls', 't_cls'], \
                     index = df_x.index)

df_x = pd.concat([df_x, df_x2], axis=1)
print(df_x.head(3))

# 데이터 분할 ( train / test )
train_x, test_x, train_y, test_y = train_test_split(df_x, df_y)

# n_estimators : 의사결정하는 트리 수
model = RandomForestClassifier(criterion='entropy', n_estimators=100)
model.fit(train_x, train_y)

pred = model.predict(test_x)

print('예측값 : ', pred[:5])
print('실제값 : ', np.array(test_y[:5]))

print('분류 정확도 ; ', sum(test_y == pred) / len(test_y))
from sklearn.metrics import accuracy_score
print('분류 정확도 : ', accuracy_score(test_y, pred))

