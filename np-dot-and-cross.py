# problem-link = https://www.hackerrank.com/challenges/np-dot-and-cross/problem?h_r=next-challenge

import numpy as np
N = int(input())
A = []
B = []

for i in range(N):
    A_row = list(map(int, input().strip().split()))
    A.append(A_row)

for i in range(N):
    B_row = list(map(int, input().strip().split()))
    B.append(B_row)

A_array = np.array(A)
B_array = np.array(B)

print(np.dot(A, B))
