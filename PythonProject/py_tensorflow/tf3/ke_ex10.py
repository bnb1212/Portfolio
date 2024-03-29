'''=============================================
로지스틱 회귀 분석 소스) 1.x
============================================='''
'''
import tensorflow.compat.v1 as tf   # tf2.x 환경에서 1.x 소스 실행 시
tf.disable_v2_behavior()            # tf2.x 환경에서 1.x 소스 실행 시

x_data = [[1,2],[2,3],[3,4],[4,3],[3,2],[2,1]]
y_data = [[0],[0],[0],[1],[1],[1]]

# placeholders for a tensor that will be always fed.
X = tf.placeholder(tf.float32, shape=[None, 2])
Y = tf.placeholder(tf.float32, shape=[None, 1])
W = tf.Variable(tf.random_normal([2, 1]), name='weight')
b = tf.Variable(tf.random_normal([1]), name='bias')

# Hypothesis using sigmoid: tf.div(1., 1. + tf.exp(tf.matmul(X, W)))
hypothesis = tf.sigmoid(tf.matmul(X, W) + b)

# 로지스틱 회귀에서 Cost function 구하기
cost = -tf.reduce_mean(Y * tf.log(hypothesis) + (1 - Y) * tf.log(1 - hypothesis))

# Optimizer(코스트 함수의 최소값을 찾는 알고리즘) 구하기
train = tf.train.GradientDescentOptimizer(learning_rate=0.01).minimize(cost)

predicted = tf.cast(hypothesis > 0.5, dtype=tf.float32)
accuracy = tf.reduce_mean(tf.cast(tf.equal(predicted, Y), dtype=tf.float32))

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for step in range(10001):
        cost_val, _ = sess.run([cost, train], feed_dict={X: x_data, Y: y_data})
        if step % 200 == 0:
            print(step, cost_val)

    # Accuracy report (정확도 출력)
    h, c, a = sess.run([hypothesis, predicted, accuracy],feed_dict={X: x_data, Y: y_data})
    print("\nHypothesis: ", h, "\nCorrect (Y): ", c, "\nAccuracy: ", a)
'''

import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation

np.random.seed(0)

x = np.array([[1, 2], [2, 3], [3, 4], [4, 3], [3, 2], [2, 1]])
y = np.array([[0], [0], [0], [1], [1], [1]])

# 모델 설정 (unit, input_dim 등)
model = Sequential([
    Dense(units=1, input_dim=2),  # input_shape=(2,)
    Activation('sigmoid')

])

# compile
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# 모델 학습(fitting)
model.fit(x, y, epochs=1000, batch_size=1, verbose=1)
m_evalu = model.evaluate(x, y)
print(m_evalu)
# print(m_evalu‎)  # [0.209698(loss),  1.0(정확도)]

pred = model.predict(np.array([[1, 2], [10, 5]]))
print('예측 결과 : ', pred)  # [[0.16490099] [0.9996613 ]]
print('예측 결과 : ', np.squeeze(np.where(pred > 0.5, 1, 0)))  # [0 1]

