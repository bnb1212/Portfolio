'''====================================================
단순 선형 회귀 모델 : 작성방법 3가지
공부시간에 따른 성적 점수 예측
===================================================='''

import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras import optimizers
import numpy as np

x_data = np.array([1, 2, 3, 4, 5], dtype=np.float32)
y_data = np.array([11, 32, 53, 64, 70], dtype=np.float32)
print(np.corrcoef(x_data, y_data))
# 상관관계는 최소한 0.35이상이어야 의미가 있다.
# 상관관계는 있지만 인과관계가 없다면, 회귀분석을 하지 않는다.

print('\n----------모델작성 방법1\n--------')
# 모델 작성 1 : 완전 연결 모델
model = Sequential() 
model.add(Dense(1, input_dim=1, activation='linear'))  # 레이어 추가

opti = optimizers.SGD(lr=0.01)
model.compile(opti, loss='mse', metrics='mse')  # MSE 평균 제곱 오차

model.fit(x=x_data, y=y_data, batch_size=1, epochs=1, verbose=1)

loss_metrics = model.evaluate(x_data, y_data)
print('loss_metrics :', loss_metrics)

from sklearn.metrics import r2_score
print('설명력 :', r2_score(y_data, model.predict(x_data)))

print('실제값:', y_data)
print('예측값:', model.predict(x_data))
print('새값 예측:', model.predict([6.5, 2.1]).flatten())

import matplotlib.pyplot as plt
plt.plot(x_data, model.predict(x_data), 'b', x_data, y_data, 'ko')
plt.show()

print('\n----------모델작성 방법2\n--------')
# 모델 작성 2 : function api를 사용 ; 방법 1에 비해 유연한 모델을 작성할 수 있다
from tensorflow.keras.layers import Input
from tensorflow.keras.models import Model

inputs = Input(shape=(1,))

# 히든레이어 1개
# output = Dense(1, activation='linear')(inputs)

# 히든레이어 2개 
output1 = Dense(2, activation='linear')(inputs)
outputs = Dense(1, activation='linear')(output1)  # 히든 레이어 2개

model2 = Model(inputs, outputs)

opti = optimizers.SGD(lr=0.001)
model2.compile(opti, loss='mse', metrics='mse')
model2.fit(x=x_data, y=y_data, batch_size=1, epochs=100, verbose=1)

# 모델 평가
loss_metrics = model.evaluate(x_data, y_data)
print('loss_metrics: ', loss_metrics)

print('실제값2:', y_data)
print('예측값2:', model2.predict(x_data).flatten())

print('\n----------모델작성 방법 3-1\n--------')


# 모델 작성 3-1 : sub classing 사용, Model을 상속
class MyModel(Model):

    def __init__(self):
        super(MyModel, self).__init__()
        self.d1 = Dense(5, activation='linear')
        self.d2 = Dense(1, activation='linear')
        
    def call(self, x):  # x는 입력 매개 변수 <==  모델.fit(), 모델.evaluate(), 모델.predict()
        x = self.d1(x)
        return self.d2(x)


model3 = MyModel()

opti = optimizers.SGD(lr=0.01)  # 이하 방법 1과 동일
model2.compile(opti, loss='mse', metrics='mse')
model2.fit(x=x_data, y=y_data, batch_size=1, epochs=100, verbose=1)

print('실제값3:', y_data)
print('예측값3:', model2.predict(x_data).flatten())

print('\n----------모델작성 방법3-2--------\n')
# 모델 작성 3-2 : sub classing 사용, Layer를 상속
from tensorflow.keras.layers import Layer


class Linear(Layer):

    def __init__(self, units=1):
        super(Linear, self).__init__()
        self.units = units
        
    def build(self, input_shape):
        self.w = self.add_weight(shape=(input_shape[-1], self.units),
                                 initializer='random_normal',
                                 trainable=True)  # trainable = True Back Propergation 진행
        
        self.b = self.add_weight(shape=(self.units, ),
                                 initializer='zeros',
                                 trainable=True)
        
    def call(self, inputs):
        return tf.matmul(inputs, self.w) + self.b
    
class MyMLP(Model):
    def __init__(self):
        super(MyMLP, self).__init__()
        self.linear1 = Linear(1) 
#         self.linear3 =Linearer(3)
        self.linear2 = Linear(1)
            
    def call(self, inputs):
        return self.linear1(inputs) # 레이어 1개
        # x = self.linear1(inputs)  # 레이어 2개
        # return self.linear1(x))
    
model4 = MyMLP()
model4.compile(opti, loss='mse', metrics='mse')
model4.fit(x=x_data, y=y_data, batch_size=1, epochs=100, verbose=1)

print('실제값3:', y_data)
print('예측값3:', model4.predict(x_data).flatten())