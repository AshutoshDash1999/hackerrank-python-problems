# problem-link = https://www.hackerrank.com/challenges/np-shape-reshape/problem
# first the space seperated input are taken then converted into
# list. Then it was passed on to the array function.
# By default the input values are string so they are coverted to int ans in the next step
# the array is formed with the required format

import numpy as np
input_values = input().strip().split()
input_values = np.array(input_values, int)
final_shape = np.reshape(input_values, (3,3))
print(final_shape)


