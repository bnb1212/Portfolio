'''==============================================
RNN 이해를 위해 4개의 숫자를 입력하고 그 다음 숫자 예측하기
SimpleRNN -> LSTM -> GRU 순으로 나옴

==============================================='''

import tensorflow as tf
import numpy as np

x = []
y = []

# 데이터 만들기
for i in range(6):
    lst = list(range(i, i + 4))
    x.append(list(map(lambda c:[c / 10], lst)))
    y.append((i + 4)/10)
     
x = np.array(x)
y = np.array(y)
print(x, np.shape(x))
print(y, np.shape(y))

for i in range(len(x)):
    print(x[i], y[i])
    
print()
# 여기에선 결과만 간단히 보자. 실무에선 좀더 세심히 설정해야하겠다
model = tf.keras.Sequential([
#     tf.keras.layers.SimpleRNN(units=10, activation='tanh', input_shape=[4, 1]),
    tf.keras.layers.GRU(units=10, activation='tanh', input_shape=[4, 1]),
    
    tf.keras.layers.Dense(1)
    ])

model.compile(optimizer='adam', loss='mse')
model.summary()
model.fit(x, y, epochs=100, verbose=0)
print(f'예측값: {model.predict(x).flatten()}')
print(f'실제값: {y}')

# 학습되지 않은 새 데이터 예측
print(model.predict(np.array([[[0.6], [0.7], [0.8], [0.9]]])))
print(model.predict(np.array([[[-0.2], [-0.1], [0.0], [0.1]]])))
