# tf 변수 구조
import tensorflow as tf
 
g1 = tf.Graph()
 
# 특정 자원을 처리하고 자동 close하기
# as_default
# with g1.as_default() as g1:
#     c1 = tf.constant(1, name='c_one')
#     print(c1)
#     print(type(c1))
#     print(c1.op)
#     # as_graph_def
#     print(g1.as_graph_def())
     
# print(c1)
 
# print('------------------------------------------------------------')
# g2 = tf.Graph()
#  
# with g2.as_default() as g2:
#     v1 = tf.Variable(initial_value=1, name='v1')
#     print(v1)
#     print(type(v1))
#     print(v1.op)
#     print(g2.as_graph_def())
