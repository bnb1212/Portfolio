'''==========================================
CNN (Convolution neural network) + Dense : image(최적화), text 분류에 효과적
Convolution : feature extraction 역할
CNN의 약점 : 연산량(이미지)이 많아 속도가 좀 느리다
=========================================='''

import tensorflow as tf
from tensorflow.keras import datasets, layers, models
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

# model
model = models.Sequential()

# CNN 
model.add(layers.Conv2D(64, kernel_size=(3, 3), padding='valid', activation='relu', input_shape=(28, 28, 1)))
model.add(layers.MaxPool2D(pool_size=(2, 2), strides=None))
model.add(layers.Dropout(0.2))  # 과적합 방지

model.add(layers.Conv2D(64, kernel_size=(3, 3), activation='relu'))
model.add(layers.MaxPool2D(pool_size=(2, 2), strides=None))
model.add(layers.Dropout(0.2)) 

model.add(layers.Conv2D(64, kernel_size=(3, 3), activation='relu'))
model.add(layers.MaxPool2D((2, 2)))
model.add(layers.Dropout(0.2)) 

model.add(layers.Flatten())  # fully connected layer : 이미지의 주요 특징만 추출한 CNN 결과를 1차원으로 변경

# 분류기로 분류 작업
model.add(layers.Dense(64, activation='relu'))
model.add(layers.Dropout(0.25))
model.add(layers.Dense(32, activation='relu'))
model.add(layers.Dropout(0.25))
model.add(layers.Dense(10, activation='softmax'))

model.summary()

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

from tensorflow.keras.callbacks import EarlyStopping
early_stop = EarlyStopping(monitor='loss', patience=5)

history = model.fit(x_train, y_train, batch_size=128, epochs=2, verbose=2, validation_split=0.2, callbacks=[early_stop])

history = history.history
print(history)

# evaluate
train_loss, train_acc = model.evaluate(x_train, y_train, batch_size=128, verbose=2)
test_loss, test_acc = model.evaluate(x_test, y_test, batch_size=128, verbose=2)
print('train_loss, train_acc :', train_loss, train_acc)
print('test_loss, test_acc :', test_loss, test_acc)

# 모델 저장후 읽기
model.save('fashion.hdf5')

del model

model = tf.keras.models.load_model('fashion.hdf5')

# predict
import numpy as np
print('예측값:', np.argmax(model.predict(x_test[:1])))
print('실제값:', y_test[1])

# 시각화
import matplotlib.pyplot as plt

def plot_acc(title=None):
    plt.plot(history['accuracy'])
    plt.plot(history['val_accuracy'])
    if title is not None:
        plt.title(title)
    plt.xlabel('epochs')
    plt.xlabel('accuracy')
    plt.legend(['train data', 'validation data'], loc=4)
    
plot_acc('accuracy')
plt.show()

plot_acc('loss')
plt.show()

