# problem link = https://www.hackerrank.com/challenges/np-concatenate/problem

# I didnt use numpy.concatenate  but still code runs
# It would be nice if you can suggest me the same.

import numpy as np
n_m_p = input().strip().split()
n = int(n_m_p[0])
m = int(n_m_p[1])
p = int(n_m_p[2])
n_m = n+m # since the output wants to be in N+M format so i added them
np_array = []  # parent list

for i in range(n_m): #  taking input for N+M arrays
    row = input().strip().split()
    row_list = list(map(int, row))
    np_array.append(row_list)

np_array = np.array(np_array)

print(np_array)