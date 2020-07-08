'''===============================================
다항 분류 : softmax 활성화 함수 사용
==============================================='''

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.utils import to_categorical
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

np.random.seed(1)

xdata = np.random.random_sample((1000, 12))
ydata = np.random.randint(10, size=(1000, 1))

# one hot encoding
ydata = to_categorical(ydata, num_classes=10)
print(xdata[:2])
print(ydata[:2])

model = Sequential()
# 노드보다 레이어의 갯수를 적당히 늘리는 것이 효과적이라고 한다.
# 노드나 레이어의 수를 늘리면 더 정확해지지면 비용이 당연히 늘어난다.
model.add(Dense(100, input_shape=(12,), activation='relu'))
model.add(Dense(50, activation='relu'))
model.add(Dense(10, activation='softmax'))
print(model.summary())
# 컴파일
# (1) model.compile(optimizer="sgd")
# (2) model.compile(optimizer="rmsprop")

# Label 값이 10개나 된다. 따라서 loss를 categorical_crossentropy로 준다.  
model.compile(optimizer="adam", loss="categorical_crossentropy", metrics=['acc']) 

hist = model.fit(xdata, ydata, epochs=500, batch_size=32, verbose=2)
model_eval = model.evaluate(xdata, ydata)
print("model_eval : ", model_eval)

print("예측값 : ", [np.argmax(i) for i in (model.predict(xdata[:5]))])
print("실제값 : ", [np.argmax(i) for i in ydata[:5]])

# 시각화
plt.plot(hist.history['loss'])
plt.plot(hist.history['acc'])
plt.show()

# 새로운 값 예측
x_new = np.random.random_sample((1,12))
print(x_new)
pred = model.predict(x_new)
print("pred 합 : ", np.sum(pred))
print(pred)
print(np.argmax(pred))
