# constant() : 텐서를 직접 기억
# Variable() : 텐서가 저장된 주소를 기억

import tensorflow as tf
import numpy as np

a = 10
print(a, type(a))
print('--------')
b = tf.constant(10)
print(b, type(b))
print('---------')
c = tf.Variable(10)
print(c, type(c))

print()
# constant와 variable 비교
# node1 = tf.constant(3.0, tf.float32)
# node2 = tf.constant(4.0)
node1 = tf.Variable(3.0, tf.float32)
node2 = tf.Variable(4.0)
print(node1)
print(node2)

node3 = tf.add(node1, node2)
print(node3)

# 데이터는 Tensor, Tensor간 연결을 시켜주는 edge, 이들은 Graph에 위에 있다.
print('------------------------------------------')
# v = tf.Variable(1)
v = tf.Variable(2)


@tf.function
def find_next_odd():
    abc()  # autograph 지원 함수가 다른 함수를 호출하면 해당 함수도 autograph가 됨
    v.assign(v + 1)
    if tf.equal(v % 2, 0):
        v.assign(v + 10)


def abc():
    print('abc')


find_next_odd()
print(v.numpy())

print('\n-----~1 ~3 까지 숫자 증가-------\n')


def func():
    imsi = tf.constant(0)
    su = 1
    for _ in range(3):
        imsi = tf.add(imsi, su)  # 누적
    return imsi

    
kbs = func()
print(kbs.numpy(), ' ', np.array(kbs))

print('----------------------------')
imsi = tf.constant(0)


def func2():
    su = 1 
    global imsi
    for _ in range(3):
        imsi = tf.add(imsi, su)
    return imsi


# mbc = func2()
# print(mbc.numpy())
mbc = func2
print(mbc().numpy())

print('$$$$$$$$')


def func3():
    imsi = tf.Variable(0) # imssi = 0
    su = 1
    for _ in range(3):
#         imsi = tf.add(imsi, su) #누적
        imsi.assign_add(su)
    return imsi


kbs = func3()
print(kbs.numpy())

print()

print('-----------------------------------------------')
imsi = tf.Variable(0)
# autograph 추가
@tf.function
def func4():
#     imsi = tf.Variable(0)  # Value Error
    su = 1
    for _ in range(3):
        imsi.assign_add(su)
    return imsi


mbc = func4()
print(mbc.numpy())

# 구구단 출력
print('\n--------- 구구단 출력 -----------------')


# @tf.function
def gugu1(dan):
    su = 0
#     aa = tf.constant(5)
#     print(aa.numpy()) # autograph 내에서는 .numpy() 사용 불가
    for _ in range(9):
        su = tf.add(su, 1)
        print('{} x {} = {:2}'.format(dan, su, dan * su))
        # TypeError : unsuported format string passed to Tensor.__format__

        
gugu1(3)
print()

def gugu2(arg):
    for i in range(1, 10):
        result = tf.multiply(arg ,i)
        print("{} * {} = {}".format(arg, i, result))
        
gugu2(5)
