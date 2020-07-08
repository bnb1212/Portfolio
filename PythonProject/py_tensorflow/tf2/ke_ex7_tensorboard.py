'''==================================================
다중 선형회귀, 텐서보드(모델의 구조 및 학습 진행 결과를 시각화 틀)
=================================================='''

import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras import optimizers
import numpy as np
import matplotlib.pyplot as plt

x_data = np.array([[70, 85, 80], [71, 89, 88], [50, 45, 70], [99, 90, 90], [50, 15, 10]])
y_data = np.array([80, 85, 55, 95, 20])

model = Sequential()
# model.add(Dense(1, input_dim = 3, activation='linear')) # 레이어 1개
model.add(Dense(6, input_dim=3, activation='linear'))  # 레이어 복수
model.add(Dense(3, activation='linear'))  # 레이어 복수
model.add(Dense(1, activation='linear'))  # 레이어 복수

print(model.summary())

from sklearn.metrics import r2_score
print('설명력:', r2_score(y_data, model.predict(x_data)))

# 텐서보드 : 시행착오를 최소화 할 수 있다.
from tensorflow.keras.callbacks import TensorBoard
tb = TensorBoard(
        log_dir='.\\mylog',
        histogram_freq=True,
        write_graph=True,
        
    )

opti = optimizers.Adam(lr=0.1)
model.compile(optimizer=opti, loss='mse', metrics=['mse'])
history = model.fit(x_data, y_data, batch_size=1, epochs=100, verbose=1, callbacks=[tb])
plt.plot(history.history['loss'])
plt.xlabel('epochs')
plt.ylabel('loss')
plt.show()

print(model.predict(x_data))
x_new = np.array([[20, 30, 70], [100, 70, 30]])
print('예상 점수 :', model.predict(x_new))

