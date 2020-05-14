# problem-link = https://www.hackerrank.com/challenges/np-inner-and-outer/problem?h_r=next-challenge

import numpy as np
A = np.array(list(map(int, input().strip().split())))
B = np.array(list(map(int, input().strip().split())))
# A = np.array(A)
# B = np.array(B)
print(np.inner(A,B), np.outer(A,B), sep ='\n')