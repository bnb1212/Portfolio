'''=========================================
텐서플로우 첫 실습
========================================='''
# 장치 확인
# from tensorflow.python.client import device_lib
# print(device_lib.list_local_devices())

import tensorflow as tf

# 버전 확인
print(tf.__version__)
print(tf.keras.__version__)
print('GPU 사용 가능 여부 : ', '가능' if tf.config.list_physical_devices('GPU') else '불가능')

# tensor의 이해 : tf의 기본 구성 요소. 데이터를 위한 컨테이너로 대게의 경우 수치 데이터
# 임의 차원 갯수를 가지는 행렬의 일반화된 객체이다.

# 상수 정의(상수 tensor를 생성)
print(tf.constant(1))  # 스칼라(scala) : 0 tensor
print(tf.constant([1]))  # 벡터(vector) : 1 tensor
print(tf.constant([[1]]))  # 행렬(matrix) : 2 tensor

# 그래프는 tensor와 edge로 구성되어 있다. tensor는 데이터를 담고있는 container, edge는 데이터가 움직이는 통로같은 역할
# 합쳐서 tensorflow. 텐서의 흐름.

# tensor 객체 확인 rank
print(tf.rank(tf.constant(1.)), ' ', tf.rank(tf.constant([[1]]))) 
print(tf.constant(1.).get_shape(), ' ', tf.rank(tf.constant([[1]])))

print()
# tensor간 연산
a = tf.constant([1, 2])
b = tf.constant([3, 4])
c = a + b
c = tf.add(a, b)

print(c, type(c))

print()
# tensor 형변환
# d = tf.constant([3])
d = 3  # tensor로 자동 변환
d = tf.constant([[3]])

# Broadcast연산
e = c + d
print(e)

# 상수를 tensor화
print(7, type(7))
print(tf.convert_to_tensor(7))
print(tf.cast(7, tf.float32))

# numpy의 ndarray와 tensor 사이에 자동 변환
import numpy as np
arr = np.array([1, 2])
print(arr, ' ', type(arr))
tfarr = tf.add(arr, 5)
print(tfarr)
print(tfarr.numpy(), ' ', type(tfarr.numpy()))
print(np.add(tfarr, 3))