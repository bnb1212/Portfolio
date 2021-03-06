'''==========================================================
회귀분석 예비 실습 : loss(cost, 손실)가 최소가 되는 기울기(weight) 구하기
=========================================================='''
import tensorflow as tf
import matplotlib.pyplot as plt
# feature
x = [1, 2, 3]

# label(class)
y = [1, 2, 3]

w_val = []
cost_val = []

for i in range(-30, 50):
    feed_w = i * 0.1 # 기울기 값
    # print(feed_w)
    hypothesis = tf.multiply(feed_w, x) + 0
    cost = tf.reduce_mean(tf.square(hypothesis -y))
    #print(cost.numpy())
    cost_val.append(cost)
    w_val.append(feed_w)
    print(str(i) + ': '+ ', cost:' + str(cost.numpy()) + ', w:' + str(feed_w))

plt.plot(w_val, cost_val)
plt.xlabel('weight')
plt.xlabel('cost')
plt.show()