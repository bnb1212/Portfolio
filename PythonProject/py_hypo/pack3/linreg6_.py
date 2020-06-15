'''===========================================================================
평균 제곱 오차(Mean squared error - mse)
머신러닝 뿐만 아니라 영상처리 영역에서도 자주 사용되는 추측값에 대한 정확성 측정 방법. 
간단히 말하면 오차의 제곱에 대해 평균을 취한 것이다. 
작을 수록 원본과의 오차가 적은 것이므로 추측한 값의 정확성이 높은 것. 
이것을 근거로 최소평균제곱오차, 평균제곱근오차 등이 있다. 

평균 제곱근 편차(Root Mean Square Deviation; RMSD) 또는 평균 제곱근 오차(Root Mean Square Error; RMSE)는 추정 값 또는 모델이 예측한 값과 실제 환경에서 관찰되는 값의 차이를 다룰 때 흔히 사용하는 측도이다. 
정밀도(precision)를 표현하는데 적합하다. 
각각의 차이값은 잔차(residual)라고도 하며, 평균 제곱근 편차는 잔차들을 하나의 측도로 종합할 때 사용된다
============================================================================'''
# from sklearn.metrics import mean_squared_error
# import numpy as np


# lin_mse = mean_squared_error(y, pred)
# lin_rmse = np.sqrt(lin_mse)
# print("평균 제곱 오차 : ", lin_mse)
# print("평균 제곱근 편차 : ", lin_rmse)