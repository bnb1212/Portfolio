'''
AutoEncoder (비지도학습의 일종) - 입력 데이터의 특징을 효율적으로 담아낸 새로운 이미지 생성
부족한 이미지 학습 데이터를 만들 수 있다.
인코더와 디코더 영역으로 분리된다.
'''

from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential, Model
from tensorflow.keras.layers import Conv2D, MaxPooling2D, UpSampling2D, Reshape
import plotly.express as px
import matplotlib.pyplot as plt 
import numpy as np

(x_train, _), (x_test, _) = mnist.load_data()
x_train = x_train.reshape(x_train.shape[0], 28, 28, 1).astype('float32') / 255
x_test = x_test.reshape(x_test.shape[0], 28, 28, 1).astype('float32') / 255

# print(x_train[:2])

# model
model = Sequential()

# encoder : 고차원 입력 데이터를 저차원 벡터로 압축
model.add(Conv2D(16, kernel_size=3, padding='same', input_shape=(28, 28, 1), activation='relu'))
model.add(MaxPooling2D(pool_size=2, padding='same'))
model.add(Conv2D(8, kernel_size=3, padding='same', activation='relu'))
model.add(MaxPooling2D(pool_size=2, padding='same'))
model.add(Conv2D(8, kernel_size=3, padding='same', strides = 2, activation='relu'))

# decoder : 저차원 압축 저차원 벡터를 고차원 데이터로 압축해제
model.add(Conv2D(8, kernel_size=3, padding='same', activation='relu'))
model.add(UpSampling2D())
model.add(Conv2D(8, kernel_size=3, padding='same', activation='relu'))
model.add(UpSampling2D())
model.add(Conv2D(16, kernel_size=3, activation='relu'))
model.add(UpSampling2D())
model.add(Conv2D(1, kernel_size=3, padding='same', activation='sigmoid'))

print(model.summary())

model.compile(optimizer='adam', loss='binary_crossentropy')
model.fit(x_train, x_train, epochs=10, batch_size=128,
          validation_data=(x_test, x_test), verbose=2)

random_test = np.random.randint(x_test.shape[0], size=5)
ae_imgs = model.predict(x_test)

for i, image_idx in enumerate(random_test):
    ax = plt.subplot(2, 7, i + 1)
    plt.imshow(x_test[image_idx].reshape(28, 28))
    ax.axis('off')
    ax = plt.subplot(2, 7, 7 + i, 1)
    plt.imshow()
    
