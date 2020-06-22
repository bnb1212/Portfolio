# 변수
import tensorflow as tf
import numpy as np

# 변수형 tensor에 scala 값 기억
print('변수형 tensor에 scala 값 기억\n')
f = tf.Variable(1.0)
v = tf.Variable(tf.ones((2,)))
m = tf.Variable(tf.ones((2, 1)))
print(f)
print(v, v.numpy())
print(m)

print('\n--scala 배열 값 핟당하기(assign)--\n')
# 상수(0차원 tensor)
v1 = tf.Variable(1) 
print(v1)
v1.assign(10)
print(v1, ' ', v1.numpy(), ' ', type(v1))

print('\n-- 1차원 배열 값 핟당하기(assign)--\n')
# 1차원 tensor (vector)
v2 = tf.Variable(tf.ones(shape=(1)))
v2.assign([20])
print(v2, ' ', type(v2))

print('\n--2차원 배열 값 핟당하기(assign)--\n')
# 2차원 tensor (vector)
v3 = tf.Variable(tf.ones(shape=(1, 2)))
v3.assign([[30, 40]])
print(v3, ' ', type(v3))

print()
v1 = tf.Variable([3])
v2 = tf.Variable([5])
v3 = v1 * v2 + 10
print(v3.numpy())

var = tf.Variable([1, 2, 3, 4, 5], dtype=tf.float32)
result1 = var + 10
print(result1)

w = tf.Variable(tf.ones(shape=(1,)))
b = tf.Variable(tf.ones(shape=(1,)))
w.assign([3])
b.assign([2])


def func1(x):
    return w * x + b


out_a1 = func1([3])
print('out_a1 : ', out_a1)

print()

w = tf.Variable(tf.zeros(shape=(1, 2)))
b = tf.Variable(tf.zeros(shape=(1,)))
w.assign([[2, 3]])
b.assign([2])


# autograph 기능(내부적으로 tf.Graph + tf.Session) : 속도가 빨라진다.
@tf.function
def func2(x):
    return w * x + b


out_a2 = func2([3])
print('out_a2 : ', out_a2)

print('---------------------------------------')

w = tf.Variable(tf.keras.backend.random_normal([5, 5], mean=0, stddev=0.3))
# print(w)
print(w.numpy().mean())
print(np.mean(w.numpy()))
b = tf.Variable(tf.zeros([5]))
print(b * w)

print()

rand1 = tf.random.normal([4], 0, 1)
print('rand1 : ', rand1)
# 난수발생 uniform
rand2 = tf.random.uniform([4], 0, 1)
print('rand1 : ', rand1)

# 변수 치환
aa = tf.ones((2, 1))
print(aa.numpy())
m = tf.Variable(tf.zeros((2, 1)))

m.assign(aa)
print(m.numpy())

m.assign(m + 10)
print(m.numpy())

m.assign_add(aa)
print(m.numpy())

m.assign_sub(aa)
print(m.numpy())
