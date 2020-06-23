'''================================================
케라스 실습
================================================'''

import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation
from tensorflow.keras.optimizers import SGD, Adam, RMSprop

# 1) 논리회로 모델 작성
# 데이터 수집 및 가공
x = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([0, 1, 1, 1])
print(x)
print(y)

# 2) 모델 생성(설정)
model = Sequential([
    Dense(input_dim=2, units=1),
    Activation('sigmoid')
    ])

model = Sequential()
model.add(Dense(1, input_dim=2))
model.add(Activation('sigmoid'))

# 3) 학습 process 생성(컴파일)
# model.compile(optimizer='sgd', loss='binary_crossentropy', metrics=['accuracy'])
# model.compile(optimizer='rmsprop', loss='binary_crossentropy', metrics=['accuracy'])
# model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy']) # 강추
# model.compile(optimizer=SGD(lr=0.1, momentum=0.8), loss='binary_crossentropy', metrics=['accuracy'])
model.compile(optimizer=RMSprop(lr=0.1), loss='binary_crossentropy', metrics=['accuracy'])
model.compile(optimizer=Adam(lr=0.1), loss='binary_crossentropy', metrics=['accuracy'])
# 경우에 따라서는 Rmsprop이 좋은 경우도 있다. 

# 4) 모델 학습(EPOCH 학습횟수) / batch_size : 말하자면 답지보는 횟수
model.fit(x, y, epochs=10, batch_size=1, verbose=1)

# 5) 모델 평가
loss_metrics = model.evaluate(x, y)
print(loss_metrics)  # 분류 정확도

# 6) 예측값 출력
pred = model.predict(x)
print('pred1 :', pred)
pred = (model.predict(x) > 0.5).astype('int32')
print('pred2 :', pred)
pred = model.predict_classes(x)
print('pred3 :', pred)

print('-------------------------------------------')
# 모델 저장
model.save('test.hdf5')
del model

# 모델 읽기
from tensorflow.keras.models import load_model
model2 = load_model('test.hdf5')

pred3 = (model2.predict(x) > 0.5).astype('int32')
print('pred3 :', pred3)






