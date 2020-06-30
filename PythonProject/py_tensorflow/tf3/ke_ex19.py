'''==============================================
Fashion MNIST DataSet 패션 이미지 분류 예측
=============================================='''
import tensorflow as tf
import sys
from tensorflow.python.keras.callbacks import EarlyStopping

'''
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.fashion_mnist.load_data()
print(f"{x_train.shape} {y_train.shape}")
print(f"{x_test.shape} {y_test.shape}")
print(x_train[0])
print(y_train[0], set(x_train))
 
for i in x_train[0]:
    for j  in i:
        sys.stdout.write('%s '%j)
    sys.stdout.write("\n")
         
         
print(y_train[0])

import matplotlib.pyplot as plt
plt.imshow(x_train[0].reshape(28, 28), cmap='Greys')
plt.show()
'''

