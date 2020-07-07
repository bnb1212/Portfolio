'''============================================
소스파일 : test.py
파일설명 : 데이터 분석 리포트 작성 테스트
작성자 : 이지운
버전 : 0.0
생성일자 : 2020-07-01
최종 수정 일자 :2020-07-03
최종 수정자 : 이지운
최종 수정 내용 : 
============================================'''
'''
import pandas as pd
from sklearn.preprocessing._data import MinMaxScaler
from sklearn.model_selection import train_test_split

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras import optimizers
from sklearn.metrics import r2_score
import seaborn as sns
import matplotlib.pyplot as plt
import django_pandas


# --------- 새로운 폰트 시도!! 일단 보류 -----------------
# import matplotlib.font_manager as fm
# 
# # 설치된 폰트 출력
# font_list = [font.name for font in fm.fontManager.ttflist]
# print(font_list)
import numpy as np
import pandas as pd
# plotly 라이브러리 불러오기
from plotly.offline import plot 

data = pd.read_excel('cri.xlsx', index=None)
# print(data)
# print(data.info())
# print(data.replace())

data_1 = data.iloc[:, :2]
# data_1 = data_1.astype(float)
print(data_1)
print(data_1.corr())

# feature & label 설정
x_data = data_1['기간']
# print(x_data, type(x_data))
y_data = data_1['합계발생']
# print(y_data)


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

opti = optimizers.SGD(lr=0.000000000001)
model2.compile(opti, loss='mse', metrics='mse')
model2.fit(x=x_data, y=y_data, batch_size=1, epochs=500, verbose=1)

# loss_metrics = model2.evaluate(x_data, y_data)
# print('loss_metrics: ', loss_metrics)

print('실제값2:', y_data)
print('예측값2:', model2.predict(x_data).flatten())


# 시각화
# 한글깨짐 방지
plt.rc('font', family='malgun gothic')
plt.rcParams['axes.unicode_minus'] = False
plt.rc('xtick', labelsize=8)

sns.barplot(data = data_1, x = '기간', y='합계발생')
plt.xticks(rotation=-90)
plt.show()

import matplotlib.pyplot as plt
plt.plot(x_data, model2.predict(x_data), 'b', x_data, y_data, 'ko')
plt.show()
'''
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import tensorflow as tf
from tensorflow.keras import layers

plt.rc('font', family='malgun gothic')
plt.rcParams['axes.unicode_minus'] = False

data = pd.read_excel('cri.xlsx', index=None)
# print(data)
# print(data.info())
# print(data.replace())

data_1 = data.iloc[:, :3]
# data_1 = data_1.astype(float)
print(data_1)
print(data_1.corr())

# feature & label 설정
x_data = data_1.iloc[: ,[0, 2]]
print(x_data, type(x_data))
y_data = data_1['합계발생']
# print(y_data)

# 시각화
sns.pairplot(data_1[['기간', '합계발생','합계검거']], diag_kind='kde')
plt.show()

# train / test 분리
train_dataset = data_1.sample(frac=0.7, random_state=123)
test_dataset = data_1.drop(train_dataset.index)
print(train_dataset.shape)  # (279, 8) -> (274, 8)
print(test_dataset.shape)  # (119, 8) -> (118, 8)

train_stat = train_dataset.describe()
train_stat.pop('합계발생')
train_stat = train_stat.transpose()
print(train_stat)

train_labels = train_dataset.pop('합계발생')
print(train_labels[:2])
test_labels = test_dataset.pop('합계발생')
print(test_labels[:2])


def st_func(x):  # 표준화 처리 함수(요소값 - 평균)/표준편차
    return ((x - train_stat['mean']) / train_stat['std'])


# print('st_func(10) : ',st_func(10))
# print(st_func(train_dataset[:3]))
st_train_data = st_func(train_dataset)
st_test_data = st_func(test_dataset)

print('-----------')


# 모델 작성 후 예측
def build_model():
    network = tf.keras.Sequential([
        layers.Dense(units=128, activation=tf.nn.relu, input_shape=[2]),
        layers.Dense(128, activation='relu'),
        layers.Dense(1)
    ])
#     opti = tf.keras.optimizers.RMSprop(0.001)
    opti = tf.keras.optimizers.Adam(0.001)
    network.compile(optimizer=opti, loss='mean_squared_error', metrics=['mean_squared_error', 'mean_absolute_error'])  # mse, mae 평균제곱, 평균절대
    
    return network  # model = network


model = build_model()
print(model.summary())

# fit() 전에 모델을 실행해 볼 수도 있다.
print(model.predict(st_train_data[:3]))  # 결과는 신경쓰지 않음

# 모델 훈련
epochs = 10000

# 학습 조기 종료
early_stop = tf.keras.callbacks.EarlyStopping(monitor='val_loss', patience=5)  # 같은 값이 다섯번 나오면 멈춰라

history = model.fit(st_train_data, train_labels, epochs=epochs, validation_split=0.2, verbose=2, callbacks=[early_stop])  # 여기에 텐서보드 넣을 수도있음

df = pd.DataFrame(history.history)
print(df.head(3))
print(df.columns)
# ['loss', 'mean_squared_error', 'mean_absolute_error', 'val_loss',
#        'val_mean_squared_error', 'val_mean_absolute_error'],  val_붙은거는 validation_split 이거때문에 보여

# from IPython.display import display # 참고 : jupyter 에서 실행하면 칼럼명 모두보임
# display(df.head(3))


# 시각화
def plot_history(history):
    hist = pd.DataFrame(history.history)
    hist['epoch'] = history.epoch
    
    plt.figure(figsize=(12, 8))
    
    plt.subplot(2, 1, 1)
    plt.xlabel('Epoch')
    plt.ylabel('Mean Abs Error')
    plt.plot(hist['epoch'], hist['mean_absolute_error'], label='Train Error')
    plt.plot(hist['epoch'], hist['val_mean_absolute_error'], label='Val Error')
    plt.legend()
    
    plt.subplot(2, 1, 2)
    plt.xlabel('Epoch')
    plt.ylabel('Mean Square Error')
    plt.plot(hist['epoch'], hist['mean_squared_error'], label='Train Error')
    plt.plot(hist['epoch'], hist['val_mean_squared_error'], label='Val Error')
    plt.legend()
    plt.show()

plot_history(history)
plt.close()

# 모델 평가
loss, mae, mse = model.evaluate(st_test_data, test_labels)
print(f'test dataset으로 평가  mae : {mae:5.3f}')
print(f'test dataset으로 평가  mse : {mse:5.3f}')
print(f'test dataset으로 평가  loss : {loss:5.3f}')

# 예측 : 주의 - 새로운 데이터로 예측을 원한다면 표준화 작업을 선행
test_pred = model.predict(st_test_data).flatten()  # 차원 떨어뜨려
print(f'예측값: {test_pred}')
print(f'실제값: {test_labels}')

# 설명력
from sklearn.metrics import r2_score
print('r2_score:', r2_score(test_labels, test_pred))

# 데이터 분포와 모델에 의한 선형회귀선 시각화
plt.scatter(test_labels, test_pred)
plt.xlabel('True value')
plt.ylabel('pred value')
plt.show()

# 오차 분포 확인 (정규성 : 잔차항이 정규분포를 따르는지 확인)
err = test_pred
plt.hist(err, bins=20)
plt.xlabel('pred error')
plt.show()
plt.show()
