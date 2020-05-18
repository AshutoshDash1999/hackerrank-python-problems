# problem-link = https://www.hackerrank.com/challenges/itertools-combinations/problem

from itertools import combinations as c
input_value = list(input().strip().split())

for j in range(1, int(input_value[1])+1):
    for i in list(c(sorted(input_value[0]), j)):
        print(''.join(i))