# problem-link = https://www.hackerrank.com/challenges/floor-ceil-and-rint/problem

import numpy as np
input_value = input().strip().split()
input_list = list(map(float, input_value))
input_array = np.array(input_list)
# print(input_array)
np.set_printoptions(legacy='1.13')
print(np.floor(input_array), np.ceil(input_array), np.rint(input_array), sep='\n')
