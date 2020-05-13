# problem_link = https://www.hackerrank.com/challenges/np-sum-and-prod/problem

# The given output is in space seperated, so we have to first convert it into a list.
# The first value gives the number of input rows so we will take that value and make a condition
# for a loop to take input and add that input to parent list. We will then convert the parent list
# into numpy array and apply the sum and prod function as given.


import numpy as np
input_value = input().strip().split()  # the input values are space seperated so they are coverted to list
input_value = list(map(int, input_value))  # the list values are in string format so they are coverted to int
n = input_value[0]
m = input_value[1]
# print(input_value, n, m)
li = []  # parent list

for i in range(n):  # loop for taking the number of inputs same as N
    row_input = input().strip().split()
    row_input = list(map(int, row_input))
    li.append(row_input)

li_array = np.array(li)
# print(li_array)
li_array_sum = np.sum(li_array, axis = 0)  # 0 for rows and 1 for columns
print(np.prod(li_array_sum, axis=None))
