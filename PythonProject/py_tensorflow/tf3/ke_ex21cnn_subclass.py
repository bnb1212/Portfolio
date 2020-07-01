'''======================================

========================================'''

import tensorflow as tf
from tensorflow.keras.layers import Dense, Flatten, Conv2D, MaxPool2D, Dropout
from tensorflow.keras import Model, datasets
import sys

(x_train, y_train), (x_test, y_test) = tf.keras.datasets.fashion_mnist.load_data()
print(f"{x_train.shape} {y_train.shape}")
print(f"{x_test.shape} {y_test.shape}")
print(x_train[0])
 
import matplotlib.pyplot as plt
plt.imshow(x_train[0].reshape(28, 28), cmap='Greys')
plt.show()

# 3차원을 4차원으로 구조 변경
# 이유 : 흑백, 컬러 여부 확인용 channel을 추가해야함 흑백 1, RGB 3

x_train = x_train.reshape((60000, 28, 28, 1))
print(x_train.ndim)
x_train = x_train / 255.0
print(x_train[:1])

x_test = x_test.reshape((10000, 28, 28, 1))
print(x_test.ndim)
x_test = x_test / 255.0
print(x_test[:1])

# ------------------------------------
import numpy as np
np.random.seed(1)
x = np.random.random_sample((5, 2))
print(x)
# dset = tf.data.Dataset.from_tensor_slices(x)
# print(dset)
dset = tf.data.Dataset.from_tensor_slices(x).shuffle(10000).batch(2)
print(dset)
for a in dset:
    print(a)
#-------------------------------------
# train data를 shuffle
train_ds = tf.data.Dataset.from_tensor_slices((x_train, y_train)).shuffle(60000).batch(28)
test_ds = tf.data.Dataset.from_tensor_slices((x_test, y_test)).batch(28)
print(train_ds, ' ', test_ds)


# subclassing api로 모델 생성
class MyModel(Model):

    def __init__(self):
        super(MyModel, self).__init__()
        self.conv1 = Conv2D(filters=32, kernel_size=[3, 3], padding='valid', activation='relu')
        self.pool1 = MaxPool2D((2, 2))
        
        self.conv2 = Conv2D(filters=32, kernel_size=[3, 3], padding='valid', activation='relu')
        self.pool2 = MaxPool2D((2, 2))
        
        self.flatten = Flatten(dtype='float32')
        
        self.d1 = Dense(64, activation='relu')
        self.drop1 = Dropout(rate=0.3)
        self.d2 = Dense(10, activation='softmax')
        
    def call(self, inputs):  # init에서 선언한 레이어를 불러와 network구성
        net = self.conv1(inputs)
        net = self.pool1(net)
        net = self.conv2(inputs)
        net = self.pool2(net)
        net = self.flatten(net)
        net = self.d1(net)
        net = self.drop1(net)
        net = self.d2(net)
        return net


model = MyModel()
temp_input = tf.keras.Input(shape=(28, 28, 1))

model(temp_input)
model.summary()  # 설정된 구조 확인

loss_obj = tf.keras.losses.SparseCategoricalCrossentropy()
optimizer = tf.keras.optimizers.Adam()

''' 일반적인 모델 학습 방법
# 컴파일
model.compile(optimizer=optimizer, loss=loss_obj, metrics=['acc'])
model.fit(x_train, y_train, batch_size=128, epochs=3, verbose=2,
          max_queue_size=10, workers=4, use_multiprocessing=True)
score = model.evaluate(x_test, y_test)
print(f'test loss :{score[0]}')
print(f'test acc : {score[1]}')

import numpy as np
print('예측값 :', np.argmax(model.predict(x_test[:2])))
'''

# GredientTape을 사용해 모델 학습 방법
train_loss = tf.keras.metrics.Mean()  # Compute the (weighted) mean of the given values.
train_accuracy = tf.keras.metrics.SparseCategoricalAccuracy()  # 정확도 계산

test_loss = tf.keras.metrics.Mean()  # 
test_accuracy = tf.keras.metrics.SparseCategoricalAccuracy()


@tf.function
def train_step(images, labels):
    with tf.GradientTape() as tape:
        predictions = model(images)
        loss = loss_obj(labels, predictions)
        
    gradients = tape.gradient(loss, model.trainable_variables)  # loss를 최소화하기 위한 미분값 계산
    optimizer.apply_gradients(zip(gradients, model.trainable_variables))
    
    train_loss(loss)  # 가중치 평균 계산
    train_accuracy(labels, predictions)    


@tf.function
def test_step(images, labels):
    with tf.GradientTape() as tape:
        predictions = model(images)
        loss = loss_obj(labels, predictions)
        
    gradients = tape.gradient(loss, model.trainable_variables)  # loss를 최소화하기 위한 미분값 계산
    optimizer.apply_gradients(zip(gradients, model.trainable_variables))
    
    test_loss(loss)  # 가중치 평균 계산
    test_accuracy(labels, predictions)
    
    
EPOCHS = 3
for epoch in range(EPOCHS):
    for x_train, y_train in train_ds:
        train_step(x_train, y_train)
        
    for x_test, y_test in test_ds:
        test_step(x_test, y_test)
        
    kbs = f'epochs:{epoch+1}, train_loss:{train_loss.result()}, train_acc:{train_accuracy.result()*100}, test_loss:{test_loss.result()}, test_acc{test_accuracy.result()*100}'

import numpy as np
print('예측값 :', np.argmax(model.predict(x_test[:1]), 1))
print('실제값 :', x_test[:1].numpy())
