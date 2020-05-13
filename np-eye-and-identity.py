# problem link = https://www.hackerrank.com/challenges/np-eye-and-identity/problem

import numpy as np

n_m_input = input().strip().split()
N = int(n_m_input[0])
M = int(n_m_input[1])
np.set_printoptions(legacy='1.13') # the test case is faulty so i added it. legacy is the spacing.
print(np.eye(N, M, k = 0))