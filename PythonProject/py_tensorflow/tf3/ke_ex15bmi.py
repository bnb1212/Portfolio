'''==================================
bmi 데이터
=================================='''
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Activation
import numpy as np
import pandas as pd

# https://raw.githubusercontent.com/pykwon/python/master/testdata_utf8/bmi.csv
bmi = pd.read_csv('https://raw.githubusercontent.com/pykwon/python/master/testdata_utf8/bmi.csv')
print(bmi.head(2))

# 정규화(미작업시 분류 정확도가 낮아짐)
bmi['height'] /= 200
bmi['weight'] /= 100
print(bmi.head(2))
x = bmi[['height', 'weight']].values
print(x[:2])

bclass = {'thin':[1, 0, 0], 'normal':[0, 1, 0], 'fat':[0, 0, 1]}
y = np.empty((20000, 3))

for i, v in enumerate(bmi['label']):
    y[i] = bclass[v]
print(y[:3])

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=12)
print(x_train.shape, x_test.shape, y_train.shape, y_test.shape)

# 내가 한거 틀린것
# y_data = y_data.map({'thin':0, 'normal':1, 'fat':2})
# print(y_data)
# nb_classes = 3
# y_one_hot = to_categorical(y_data, num_classes=nb_classes)
# print(y_one_hot[:1])

# 모델 생성
model = Sequential()
model.add(Dense(128, input_shape=(2,)))
model.add(Activation("relu"))
model.add(Dropout(0.2))  # 20% 데이터는 학습에서 제외하기

model.add(Dense(64))
model.add(Activation("relu"))
model.add(Dropout(0.2))  # 20% 데이터는 학습에서 제외하기

model.add(Dense(3, activation="softmax"))
model.summary()

# 컴파일
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# model train
from tensorflow.keras.callbacks import EarlyStopping

# 0.05보다 작은 값이 연속적으로 3회 이상 나오면 학습 조기 종료
es = EarlyStopping(monitor='val_loss', mode='min', baseline=0.05, patience=5)

model.fit(x_train, y_train, batch_size=64, epochs=1000, validation_split=0.2, verbose=2, callbacks=[es])

# model evaluate
m_score = model.evaluate(x_test, y_test)
print('loss :', m_score[0])
print('accuracy:', m_score[1])

# predict
print('예측값: ', np.argmax(model.predict(x_test[:1]), axis=1))
print('실제값: ', y_test[:1], ' ',np.argmax(y_test[:1]))

print()
# new data
print('예측값: ', np.argmax(model.predict(np.array([[187/200, 55/100]])), axis=1))
print('예측값: ', np.argmax(model.predict(np.array([[157/200, 65/100]])), axis=1))