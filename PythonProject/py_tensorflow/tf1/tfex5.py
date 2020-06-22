# 연산자와 기본 함수
import tensorflow as tf
import numpy as np

x = tf.constant(7)
y = 3

result1 = tf.cond(x > y, lambda:tf.add(x, y), lambda:tf.subtract(x, y))
print(result1.numpy())

f1 = lambda : tf.constant(1)
print(f1())
f2 = lambda :tf.constant(2)
a = tf.constant(3)
b = tf.constant(4)

# result2 = tf.case([tf.less(a, b), f1], default=f2)
# print(result2.numpy())

print('관계')
print(tf.equal(1, 2).numpy())
print(tf.not_equal(1, 2))
print(tf.less(1, 2))
print(tf.greater(1, 2))
print(tf.greater_equal(1, 2))

print('논리')
print(tf.logical_and(True, False))

print()
kbs = tf.constant([1, 2, 2, 2, 3])
val, ind = tf.unique(kbs)
print(val)
print(ind)

print('차원 관련 ----')
ar = [[1, 2], [3, 4]]
print(tf.reduce_sum(ar))
print(tf.reduce_mean(ar))
print(tf.reduce_mean(ar, axis=0))
print(tf.reduce_mean(ar, axis=1))

print()
t = np.array([[[0, 1, 2], [3, 4, 5]], [[6, 7, 8], [9, 10, 11]]])
print(t.shape)
print(tf.reshape(t, shape=[2, 6]))
print(tf.reshape(t, shape=[-1, 6]))
print(tf.reshape(t, shape=[2, -1]))

print()
# 차원 축소 -----
print(tf.squeeze(t))
aa = np.array([[1], [2], [3], [4]])
print(aa.shape)
bb = tf.squeeze(aa)
print(bb.shape)

print()
# 차원 증가 ----- 
tarr = tf.constant([[1, 2, 3], [4, 5, 6]])
print(tf.shape(tarr))

sbs = tf.expand_dims(tarr, 0)
print(sbs, ' ', tf.shape)
sbs = tf.expand_dims(tarr, 1)
print(sbs, ' ', tf.shape)
sbs = tf.expand_dims(tarr, 2)
print(sbs, ' ', tf.shape)
sbs = tf.expand_dims(tarr, -1)
print(sbs, ' ', tf.shape)

print()
# 참고 : 텐서플로우엔 강력한 도구인 텐서보드가 있다. 
print(tf.one_hot([0, 1, 2, 0], depth=2))
print(tf.one_hot([2, 5, 1, 1], depth=4))

print()
# 정수를 실수로 형변환(casting)
print(tf.cast([1, 2, 3, 5], tf.float32))
a = 5
print(tf.cast(a > 7, tf.float32))

print()
x = [1, 4]
y = [2, 5]
z = [3, 6]
print(x, y, z)
print(tf.stack([x, y, z]))
print(tf.stack([x, y, z], axis=0))
print(tf.stack([x, y, z], axis=1))

print()
x = np.array([[0,1,2],[2,1,0]])
print(x)
print(tf.ones_like(x))
print(tf.zeros_like(x))

#...
