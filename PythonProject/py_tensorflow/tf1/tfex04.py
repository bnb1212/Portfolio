# constant() : 텐서(일반적인 상수 값)를 직접 기억    - 포인터 변수랑 같다
# Variable() : 텐서가 저장된 주소를 기억

import tensorflow as tf
import numpy as np
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'   # AVX를 지원하지 않는다는 에러 발생 시 기술함

a = 10
print(a, type(a))
print('--------------------------------------')
b = tf.constant(10)
print(b, type(b))
print('--------------------------------------')
c = tf.Variable(10)
print(c, type(c))

print()
# node1 = tf.constant(3.0, tf.float32)    # constant : tensor 변수
# node2 = tf.constant(4.0)
node1 = tf.Variable(3.0, tf.float32)    # Variable : numpy배열을 기억하고 있는 참조 변수(주소를 가지고 있음)
node2 = tf.Variable(4.0)
print(node1)
print(node2)
node3 = tf.add(node1, node2)
print(node3)

print('\n-------------------------------------')
#v = tf.Variable(1)    # v = 1 이면 12가 된다.
v = tf.Variable(2)   # v = 2 이면 3이 된다.

@tf.function
def find_next_odd():
    abc()   # autograph 지원 함수가 다른 함수를 호출하면해당 함수도 autograph가 됨.
    v.assign(v+1)
    if tf.equal(v % 2, 0):
        v.assign(v + 10)

def abc():
    print('abc')

find_next_odd()
print(v.numpy())

print('\n--1 ~ 3 까지 숫자 증가--------------------')
def func():
    imsi = tf.constant(0)   # imsi = 0
    su = 1
    for _ in range(3):
        #imsi = tf.add(imsi, su) # 누적
        imsi += su
    return imsi

kbs = func()
print(kbs.numpy(), ' ', np.array(kbs))

print('\n+++++++++++++++++++++++++++++++++++++')
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

print('\n=====================================')
def func3():
    imsi = tf.Variable(0)   # imsi = 0
    su = 1
    for _ in range(3):
        #imsi = tf.add(imsi, su) # 누적
        imsi.assign_add(su)
    return imsi

kbs = func3()
print(kbs.numpy())

print('\n*************************************')
imsi = tf.Variable(0)
@tf.function
def func4():
    #imsi = tf.Variable(0)    # ValueError
    su = 1
    for _ in range(3):
        imsi.assign_add(su)
    return imsi

mbc = func4()
print(mbc.numpy())

print('\n구구단 출력------------------------------')
#@tf.function
def gugu1(dan):
    su = 0
    #aa = tf.constant(5)
    #print(aa.numpy())   # autograph 내에서는 .numpy() X
    
    for _ in range(9):
        su = tf.add(su, 1)
        print('{} * {} = {:2}'.format(dan, su, dan*su))
        #TypeError : unsupported format string passed to Tensor.__format__

gugu1(3)    # 3단 출력

print()
#@tf.function
def gugu2(arg):
    for i in range(1, 10):
        result = tf.multiply(arg, i)
        print('{} * {} = {}'.format(arg, i, result))
        
gugu2(5)














