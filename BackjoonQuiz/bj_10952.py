# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1WuTygMoNl4zu6PMjTsrYAvYSTdhlXzTB
"""

#===============================================================================
# while문 연습 문제 10952

# 문제
# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

# 입력
# 입력은 여러 개의 테스트 케이스로 이루어져 있다.

# 각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)

# 입력의 마지막에는 0 두 개가 들어온다.

# 출력
# 각 테스트 케이스마다 A+B를 출력한다.
#===============================================================================

i = 0
numlist = []
while(True):
    a, b = input().split()
    a = int(a)
    b = int(b)
    if (a == 0 and b == 0):
        break
    numlist.append((a, b))
    i = i + 1

i = 0
while(i < len(numlist)):
    print(numlist[i][0] + numlist[i][1])
    i = i + 1

