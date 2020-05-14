# problem-link = https://www.hackerrank.com/challenges/np-min-and-max/problem

import numpy as np
n_m = list(map(int, input().strip().split()))
N = n_m[0]
M = n_m[1]
n_m_list = np.zeros((N,M), int)

for i in range(N):
    n_m_list[i] = list(map(int, input().strip().split()))

nm_array = np.array(n_m_list)
min_list = list(np.min((nm_array), axis =1))
print(np.max(min_list))
