# Keras로 자동차 연비 예측
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import tensorflow as tf
from tensorflow.keras import layers

dataset = pd.read_csv("https://raw.githubusercontent.com/pykwon/python/master/testdata_utf8/auto-mpg.csv")
print(dataset.head(2))
print(dataset.isna().sum())
del dataset['car name']
print(dataset.head(2))
#print(dataset.info()) # 각 컬럼 정보 확인 : horsepower(object) 자료중에 ? 포함되어있었다. 물음표를 지우든 강제로 형변환을 하자

# 강제 형 변환 시 ValueError 를 무시하기 : errors = 'coerce'
dataset['horsepower'] = dataset['horsepower'].apply(pd.to_numeric,errors='coerce')
print(dataset.info())
print(dataset.isna().sum()) # NaN 확인 horsepower 6
dataset = dataset.dropna() # 누락행 날림

# 시각화
sns.pairplot(dataset[['mpg','weight','horsepower']],diag_kind='kde')
plt.show()

# train / test 분리
train_dataset = dataset.sample(frac=0.7,random_state=123)
test_dataset = dataset.drop(train_dataset.index)
print(train_dataset.shape) # (279, 8) -> (274, 8)
print(test_dataset.shape) # (119, 8) -> (118, 8)

train_stat = train_dataset.describe()
train_stat.pop('mpg')
train_stat = train_stat.transpose()
print(train_stat)

# label : 'mpg'
train_labels = train_dataset.pop('mpg')
print(train_labels[:2])
test_labels = test_dataset.pop('mpg')
print(test_labels[:2])

def st_func(x): # 표준화 처리 함수(요소값 - 평균)/표준편차
    return ((x - train_stat['mean'])/train_stat['std'])
# print('st_func(10) : ',st_func(10))
# print(st_func(train_dataset[:3]))
st_train_data = st_func(train_dataset)
st_test_data = st_func(test_dataset)

print('-----------')
# 모델 작성 후 예측
def build_model():
    network = tf.keras.Sequential([
        layers.Dense(units=64, activation=tf.nn.relu,input_shape = [7]),
        layers.Dense(64, activation='relu'),
        layers.Dense(64, activation='relu'),
        layers.Dense(1,activation = 'linear')
    ])
#     opti = tf.keras.optimizers.RMSprop(0.001)
    opti = tf.keras.optimizers.Adam(0.001)
    network.compile(optimizer=opti, loss='mean_squared_error',metrics=['mean_squared_error','mean_absolute_error']) # mse, mae 평균제곱, 평균절대
    
    return network  # model = network

model = build_model()
print(model.summary())

# fit() 전에 모델을 실행해 볼 수도 있다.
print(model.predict(st_train_data[:3])) # 결과는 신경쓰지 않음

# 모델 훈련
epochs = 2000

# 학습 조기 종료
early_stop = tf.keras.callbacks.EarlyStopping(monitor='val_loss',patience=5) # 같은 값이 다섯번 나오면 멈춰라


history = model.fit(st_train_data,train_labels,epochs=epochs,validation_split=0.2,verbose=1,callbacks = [early_stop]) # 여기에 텐서보드 넣을 수도있음

df = pd.DataFrame(history.history)
print(df.head(3))
print(df.columns)
# ['loss', 'mean_squared_error', 'mean_absolute_error', 'val_loss',
#        'val_mean_squared_error', 'val_mean_absolute_error'],  val_붙은거는 validation_split 이거때문에 보여

#from IPython.display import display # 참고 : jupyter 에서 실행하면 칼럼명 모두보임
#display(df.head(3))

# 시각화
def plot_history(history):
    hist = pd.DataFrame(history.history)
    hist['epoch'] = history.epoch
    
    plt.figure(figsize=(8,12))
    
    plt.subplot(2,1,1)
    plt.xlabel('Epoch')
    plt.ylabel('Mean Abs Error [MPG]')
    plt.plot(hist['epoch'], hist['mean_absolute_error'],label='Train Error')
    plt.plot(hist['epoch'], hist['val_mean_absolute_error'],label = 'Val Error')
    plt.ylim([0,5])
    plt.legend()
    
    plt.subplot(2,1,2)
    plt.xlabel('Epoch')
    plt.ylabel('Mean Square Error [$MPG^2$]') #mpg 2승 기호
    plt.plot(hist['epoch'], hist['mean_squared_error'],label='Train Error')
    plt.plot(hist['epoch'], hist['val_mean_squared_error'],label = 'Val Error')
    plt.ylim([0,20])
    plt.legend()
    plt.show()

plot_history(history)

# 모델 평가
loss, mae, mse = model.evaluate(st_test_data,test_labels)
print('test dataset으로 평가  mae : {:5.3f}'.format(mae))
print('test dataset으로 평가  mse : '.format(mse))
print('test dataset으로 평가  loss : '.format(loss))



# 예측 : 주의 - 새로운 데이터로 예측을 원한다면 표준화 작업을 선행
test_pred = model.predict(st_test_data).flatten() #차원 떨어뜨려
print(test_pred)

# 데이터 분포와 모델에 의한 선형회귀선 시각화
plt.scatter(test_labels,test_pred)
plt.xlabel('True value[mpg]')
plt.ylabel('pred value[mpg]')
plt.show()

# 오차 분포 확인 (정규성 : 잔차항이 정규분포를 따르는지 확인)
err = test_pred
plt.hist(err,bins=20)
plt.xlabel('pred error[mpg]')
plt.show()
plt.show()