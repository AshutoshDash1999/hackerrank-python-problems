# problem link - https://www.hackerrank.com/challenges/np-mean-var-and-std/problem

import numpy as np
dimensional_array = list(map(int, input().strip().split()))
array_list = []

for i in range(dimensional_array[0]):

    row_input = list(map(int, input().strip().split()))
    array_list.append(row_input)

final_array = np.array(array_list)
np.set_printoptions(legacy='1.13')
print(np.mean(final_array, axis=1), np.var(final_array, axis=0), np.std(final_array), sep='\n')