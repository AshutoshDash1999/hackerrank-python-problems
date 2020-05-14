# problem-link = https://www.hackerrank.com/challenges/np-linear-algebra/problem

import numpy as np

N = int(input())
A = []
for i in range(N):
    row_input = list(map(float, input().strip().split()))
    A.append(row_input)

print(round(np.linalg.det(A), 2))