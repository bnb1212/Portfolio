''' ===============================================
선형 회귀 모형 계산
================================================'''
import tensorflow as tf
import numpy as np

# feature & label
x = [1, 2, 3, 4, 5]
y = [1.2, 2.0, 3.0, 3.5, 5.5]

weight = tf.Variable(tf.random.normal((1,)))
bias_ = tf.Variable(tf.random.normal((1,)))
opti = tf.keras.optimizers.Adam()


# cost Function
def train_step(x, y):
    with tf.GradientTape() as tape:
        hypo = tf.add(tf.multiply(weight, x), bias_)
        loss = tf.reduce_mean(tf.square(tf.subtract(hypo, y)))
    
    # 미분 처리를 지원하는 gradient함수
    grad = tape.gradient(loss, [weight, bias_])
    opti.apply_gradients(zip(grad, [weight, bias_]))
    return loss

    
w_vals = []
loss_vals = []

for i in range(100):
    loss_val = train_step(x, y)
    loss_vals.append(loss_val.numpy())
    w_vals.append(weight)
#     print(loss_val)
    
print(w_vals)
print(loss_vals)

import matplotlib.pyplot as plt
plt.plot(w_vals, loss_vals, 'o--')
plt.xlabel('weight')
plt.ylabel('cost')
plt.show()

y_pred = tf.multiply(x, weight) + bias_
print(y_pred.numpy())

plt.plot(x, y, 'ro')
plt.plot(x, y_pred, 'b-')
plt.show()