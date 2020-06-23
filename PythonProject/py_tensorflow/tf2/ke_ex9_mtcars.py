'''============================================
Keras로 자동차 연비 예측
============================================'''

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import tensorflow as tf
from tensorflow.keras import layers

raw_data = pd.read_csv('https://raw.githubusercontent.com/pykwon/python/master/testdata_utf8/auto-mpg.csv')
# print(raw_data)

# 결측치 확인
# print(raw_data.isna().sum())
del raw_data['car name']
# print(raw_data.head(2))

# 강제 형 변환시 ValueError를 무시하기 : errors='coerce'
raw_data['horsepower'] = raw_data['horsepower'].apply(pd.to_numeric, errors='coerce')
# print('horse:', raw_data['horsepower'])
print(raw_data.isna().sum())  # horsepower NAN이 6개

# 시각화
sns.pairplot(raw_data[['mpg', 'weight', 'horsepower']], diag_kind='kde')
plt.show()

train_dataset = raw_data.sample(frac=0.8, random_state=0)
test_dataset = raw_data.drop(train_dataset.index)
print(train_dataset.shape)
print(train_dataset.info())
print(test_dataset)

train_stat = train_dataset.describe()
train_stat.pop('mpg')
train_stat = train_stat.transpose()
print(train_stat)

# label
train_labels = train_dataset.pop('mpg')
print(train_labels[:2])
test_labels = test_dataset.pop('mpg')
print(test_labels[:2])


# 표준화 처리 함수 :(요소값 - 평균) / 평균편차
def st_func(x): 
    return ((x - train_stat['mean']) / train_stat['std'])


# print('st_func:',st_func(10))
st_train_data = st_func(train_dataset)
st_test_data = st_func(test_dataset)

print('-------------------------------------------')


# 모델 작성 후 예측
def build_model():
    network = tf.keras.Sequential([
        layers.Dense(units=64, activation=tf.nn.relu, input_shape=[7]),
        layers.Dense(32, activation='relu'),
        layers.Dense(1, activation='linear')
    ])
    
    # opti = tf.keras.optimizers.RMSprop(0.001)
    opti = tf.keras.optimizers.Adam(0.01)
    network.compile(optimizer=opti, loss='mean_squared_error',
                   metrics=['mean_squared_error', 'mean_absolute_error'])  # mse, mae
    
    return network


model = build_model()
print(model.summary())

# fit() 전에 모델을 실행해 볼 수도 있다.
print(model.predict(st_train_data[:1]))

# 모델 훈련
epochs = 5000

# 학습 조기 종료 (patience : 5번이상 주는게 맞다)
early_stop = tf.keras.callbacks.EarlyStopping(monitor='val_loss', patience=5)
history = model.fit(st_train_data, train_labels, epochs=epochs, validation_split=0.2, verbose=1, callbacks=[early_stop])
df = pd.DataFrame(history.history)

# print(df.head(3))
# print(df.columns)
# Jupiter Notebook에서 실행가능. 칼럼명 모두 보기
# from IPython.display import display 
# display(df.head(3))


def plot_history(history):
    hist = pd.DataFrame(history.history)
    hist['epoch'] = history.epoch
    plt.figure(figsize=(8, 12))
    plt.subplot(2, 1, 1)
    plt.xlabel('Epoch')
    plt.ylabel('Mean Abs Error [MPG]')
    plt.plot(hist['epoch'], hist['mean_absolute_error'], label='Train Error')
    plt.plot(hist['epoch'], hist['val_mean_absolute_error'], label='Val Error')
    
    plt.legend()
    plt.subplot(2, 1, 2)
    plt.xlabel('Epoch')
    plt.ylabel('Mean Square Error [$MPG^2$]')  # 작은윗첨자로 2제곱이
    plt.plot(hist['epoch'], hist['mean_squared_error'], label='Train Error')
    plt.plot(hist['epoch'], hist['val_mean_squared_error'], label='Val Error')
    plt.ylim([0, 20])
    plt.legend()
    plt.show()

    
plot_history(history)

# 모델평가
loss, mae, mse = model.evaluate(st_test_data, test_labels)
print('test dataset으로 모델 평가 mae : {:5.3f}'.format(mae))
print('test dataset으로 모델 평가 mse : {:5.3f}'.format(mse))
print('test dataset으로 모델 평가 loss: {:5.3f}'.format(loss))

# 예측 : 주의 - 새로운 데이터로 예측을 원한다면 표준화 작업을 선행
test_pred = model.predict(st_test_data).flatten()
print(test_pred)

plt.scatter(test_labels, test_pred)
plt.xlabel('True value[mpg]')
plt.ylabel('pred value[mpg]')
plt.show()

# 오차 분포 확인 (정규성 : 잔차항이 정규분포를 따르는지 확인)
err = test_pred
plt.hist(err, bins=20)
plt.xlabel('pred error[mpg]')
plt.show()



