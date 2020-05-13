# problem link = https://www.hackerrank.com/challenges/np-transpose-and-flatten/problem
# taking input N and M which defines the shape of matrix


import numpy as np
n_m = input().strip().split()
n = int(n_m[0])  # coverting str to int bcoz we have to take N number of inputs
m = int(n_m[1])
array_list = []  # parent list

for i in range(n): # taking input n times
    row_input = input().strip().split()
    array_list.append(row_input)

np_array = np.array(array_list, int)  # by default the input values are strings so converting them to int
transposed_array = np.transpose(np_array)
flattened_aray = np_array.flatten()
print(transposed_array)
print(flattened_aray)