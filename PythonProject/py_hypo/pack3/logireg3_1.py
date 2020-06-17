""" Softmax 구현 """
import numpy as np

def softmax(a) :
    exp_a = np.exp(a)
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a
    
    return y

a = np.array([0.3, 2.9, 4.0])

# softmax 결과값 출력
print(softmax(a)) 

# softmax 결과값들의 합은 1이 된다.
print(sum(softmax(a)) )

""" 
Softmax는 Overflow에 취약하다.
식에 e^x 들어가기 때문에 Overflow 범위를 넘어설 수 있다. 
를 해결하기 위해서는 Softmax의 성질을 이용한다.
"""

def new_softmax(a) : 
    c = np.max(a) # 최댓값
    exp_a = np.exp(a-c) # 각각의 원소에 최댓값을 뺀 값에 exp를 취한다. (이를 통해 overflow 방지)
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a
    return y
    
a = np.array([1010, 1000, 990]) 
print(softmax(a)) # overflow
print(new_softmax(a)) # 정상적으로 출력

# 또한 softmax와 new_softmax 의 결과값을 같다.
test = np.array([1,3,6])
print('softmax', softmax(test)) # [ 0.00637746  0.04712342  0.94649912]
print('new_softmax', new_softmax(test)) # [ 0.00637746  0.04712342  0.94649912]