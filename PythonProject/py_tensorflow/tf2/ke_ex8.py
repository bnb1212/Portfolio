'''================================================
선형회귀
================================================'''

import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation
from tensorflow.keras.optimizers import Adam
from sklearn.preprocessing import MinMaxScaler 
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing._data import minmax_scale

data = pd.read_csv('https://raw.githubusercontent.com/pykwon/python/master/testdata_utf8/Advertising.csv')
del data['no']

# print(data.head(2))

# 상관관계 확인
print(data.corr())

# 정규화 : 0 ~ 1 사이로 scaling 
# -- 1 -- 
scaler = MinMaxScaler(feature_range=(0, 1))
scaler = MinMaxScaler()
xy = scaler.fit_transform(data)  # scaler.inverse_transform(xy)
print(xy[:2])

# -- 2 --
# minmax_scale의 인자 copy는 원본보존 여부 의미
# xy = minmax_scale(data, axis=0, copy=True)
# print(xy[:2])

from sklearn.model_selection import train_test_split
# 과적합 방지
# x_train, x_test, y_train, y_test = train_test_split(xy[:, 0:-1], xy[:, -1],
#                                                     test_size=0.3, random_state=123)
x_train, x_test, y_train, y_test = train_test_split(data.iloc[:, 0:-1], data.iloc[:, -1],
                                                    test_size=0.3, random_state=123)

print(x_train[:2], ' ', x_train.shape)
print(y_train[:2], ' ', y_train.shape)

model = Sequential()
model.add(Dense(20, input_dim =3))
model.add(Activation('linear'))
model.add(Dense(10))
model.add(Activation('linear'))
model.add(Dense(1))
model.add(Activation('linear'))

model.summary()

import tensorflow as tf
tf.keras.utils.plot_model(model, 'abc.png')

model.compile(optimizer=Adam(lr=0.001), loss='mse', metrics=['mse']) 
# 학습하면서 과적합 발생을 방지하기 위해 validation_split으로 한번더 7:3비율로 쪼개기(0.3)
history = model.fit(x_train, y_train, batch_size=32, epochs=100, verbose=0, validation_split=0.3) #데이터의 양이 적다면 k-fold(K겹 교차검증)
# print(history.history['loss'])
# print(history.history['mse'])
print('train: ',history.history['loss'])

# 평가(evaluate)
loss = model.evaluate(x_test, y_test, batch_size=32)
print('test_loss:',loss)

# 설명력
from sklearn.metrics import r2_score
print('r2_score:', r2_score(y_test, model.predict(x_test)))

pred = model.predict(x_test)
print('실제값 :', y_test[:5])
print('예측값 :', pred[:5].flatten())

# GraphBiz