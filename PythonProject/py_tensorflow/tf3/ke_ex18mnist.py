'''==============================================
MNIST DataSet 손글씨 이미지 분류 예측
=============================================='''
import tensorflow as tf
import sys
from tensorflow.python.keras.callbacks import EarlyStopping

(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()
print(f"{x_train.shape} {y_train.shape}")
print(f"{x_test.shape} {y_test.shape}")
# print(x_train[0])
# print(y_train[0], set(x_train))
# 
# for i in x_train[0]:
#     for j  in i:
#         sys.stdout.write('%s '%j)
#     sys.stdout.write("\n")
#         
#         
# print(y_train[0])

import matplotlib.pyplot as plt
plt.imshow(x_train[0].reshape(28, 28), cmap='Greys')
plt.show()

x_train = x_train.reshape(60000, 784).astype('float32')
x_test = x_test.reshape(10000, 784).astype('float32')
print(x_train[0])
x_train /= 255  # 정규화
x_test /= 255  # 정규화
print(x_train[0])

print(y_train[0])
print(set(y_train))
y_train = tf.keras.utils.to_categorical(y_train, 10)  # label을 원핫인코딩
y_test = tf.keras.utils.to_categorical(y_test, 10)  # label을 원핫인코딩
print(y_train[0])
# train data의 일부를 validation data로 사용
x_val = x_train[50000:60000]
y_val = y_train[50000:60000]
x_train = x_train[0:50000]
y_train = y_train[0:50000]
print(x_val.shape, ' ', x_train.shape)

print()
# 모델 작성 후 분류
model = tf.keras.Sequential()

model.add(tf.keras.layers.Dense(512, input_shape=(784,)))
model.add(tf.keras.layers.Activation('relu'))
model.add(tf.keras.layers.Dropout(0.2))

model.add(tf.keras.layers.Dense(512, input_shape=(784,)))
model.add(tf.keras.layers.Activation('relu'))
model.add(tf.keras.layers.Dropout(0.2))

model.add(tf.keras.layers.Dense(10))
model.add(tf.keras.layers.Activation('softmax'))

print(model.summary())

model.compile(optimizer=tf.keras.optimizers.Adam(),
              loss='categorical_crossentropy', metrics=['accuracy'])

es = EarlyStopping(patience=8)  # patience는 정석대로는 더 주는게 좋다
history = model.fit(x_train, y_train, epochs=1000, batch_size=128,
                    validation_data=(x_val, y_val), verbose=2,
                    callbacks=[es])

print(history.history)
print(history.history.keys())

'''
# 시각화
plt.plot(history.history['loss'], label='loss')
plt.plot(history.history['val_loss'], 'r--', label='val_loss')
plt.xlabel('epochs')
plt.ylabel('loss')
plt.legend()
plt.show()

# evaluate (평가)
score = model.evaluate(x_test, y_test, batch_size=128, verbose=1)
print(f'evaluate loss: {score[0]}')
print(f'evaluate acc: {score[1]}')

model.save('mnist_model.hdf5')

del model
'''
# 저장
model = tf.keras.models.load_model('mnist_model.hdf5')

# pred
import numpy as np

print(x_test[:1], x_test[:1].shape)
pred = model.predict(x_test[:1])
print(f"pred : {pred}")
print(f"pred : {np.argmax(pred,1)}")
print(f"실제값: {np.argmax(y_test[:1], 1)}")

from PIL import Image
im = Image.open('num1.png')
img = np.array(im.resize((28, 28), Image.ANTIALIAS).convert('L'))
# print(img)
data = img.reshape([1, 784])
data = data / 255.
# print(data)
# plt.imshow(data.reshape(28, 28), cmap='Greys')
# plt.show()

new_pred = model.predict(data)
print(f'new_pred : {np.argmax(new_pred, 1)}')
