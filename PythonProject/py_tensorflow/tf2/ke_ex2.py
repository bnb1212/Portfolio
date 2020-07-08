'''===============================================
딥러닝
================================================'''

import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation
from tensorflow.keras.optimizers import SGD, Adam, RMSprop

# 1) 논리회로 모델 작성
# 데이터 수집 및 가공
x = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([0, 1, 1, 0])
print(x)
print(y)

# 2) 모델 생성(설정)
model = Sequential([
    Dense(input_dim=2, units=1),
    Activation('relu'),
    Dense(units=1),
    Activation('sigmoid'),
    ])

model = Sequential()
# model.add(Dense(1, input_dim=2))
# model.add(Activation('sigmoid'))
model.add(Dense(5, input_dim=2, activation='relu'))
model.add(Dense(5, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

model.compile(optimizer=Adam(lr=0.01), loss='binary_crossentropy', metrics=['acc'])

# 모델 파라미터 확인
print(model.summary())

# 모니터링 결과(history) 받기
history = model.fit(x, y, epochs=100, batch_size=1, verbose=2)

loss_metrics = model.evaluate(x, y)
print('loss_metrics :', loss_metrics)

pred = (model.predict(x) > 0.5).astype('int32')
print('pred : ', pred)

print('-------------')
print(model.weights)  # dense/kernel, bias 확인
print('**************')
print('loss :', history.history['loss'])
print('acc :', history.history['acc'])

import matplotlib.pyplot as plt
plt.plot(history.history['loss'])
plt.plot(history.history['acc'])
plt.xlabel('epoch')
plt.show()

import pandas as pd
# print(pd.DataFrame(history.history)
pd.DataFrame(history.history).plot(figsize=(8., 5))
plt.grid(True)
plt.gca().set_ylim(0, 1)
plt.show()
