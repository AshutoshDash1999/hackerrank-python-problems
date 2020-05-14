# problem-link = https://www.hackerrank.com/challenges/np-array-mathematics/problem

# solution-link = https://www.hackerrank.com/challenges/np-array-mathematics/forum/comments/698200

import numpy as np
first_input = input().strip().split()
N = int(first_input[0])
M = int(first_input[1])
A = []
B = []

for i in range(N):
    A_list = list(map(int, input().strip().split()))
    A.append(A_list)

for i in range(N):
    B_list = list(map(int, input().strip().split()))
    B.append(B_list)

A = np.array(A)
B = np.array(B)
print(np.add(A, B), np.subtract(A, B), np.multiply(A, B), A//B, np.mod(A, B), np.power(A, B), sep='\n')
