# -*- coding: utf-8 -*-
"""bj_2446.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Es-R6wgTUVSVvw_9eCluRScxH9FMfkf0
"""

# ==========================================================
# 문제 2446
# 예제를 보고 규칙을 유추한 뒤에 별을 찍어 보세요.

# 입력
# 첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.

# 출력
# 첫째 줄부터 2×N-1번째 줄까지 차례대로 별을 출력한다.

# 예제 입력 1 
# 5

# 예제 출력 1 
# ********* 9 0 
#  ******* 7 1
#   ***** 5 2 
#    *** 3 3 
#     * 1 4
#    *** 3 3
#   ***** 5 2
#  ******* 7 1
# ********* 9 0

# ==========================================================

n = int(input())

for s in range(n):
    for t in range(s):
        print(" ",end="")
    for a in range(n-s):
        print("*",end="")
    for r in range(n-s-1):
        print("*",end="")
    print()

for s in range(2, n+1):
    for t in range(n-s):
        print(" ", end="")
    for a in range(s):
        print("*", end="")
    for r in range(s-1):
        print("*", end="")
    print()

