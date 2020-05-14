# problem-link : https://www.hackerrank.com/challenges/np-zeros-and-ones/problem

import numpy as np

input_list = list(map(int, input().strip().split()))

print(np.zeros((input_list), dtype = np.int))
print(np.ones((input_list), dtype = np.int))