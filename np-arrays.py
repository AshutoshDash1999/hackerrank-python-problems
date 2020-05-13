# problem link = https://www.hackerrank.com/challenges/np-arrays/problem


import numpy

def arrays(arr):  # defining a function to take input
    # complete this function
    # use numpy.array
    arr_list = list(map(float, arr))  #covert input to float
    arr_list = arr_list[::-1]  # reading list in reverse order
    array_list = numpy.array(arr_list)
    return array_list

arr = input().strip().split(' ')
result = arrays(arr)
print(result)