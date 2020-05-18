# problem-link = https://www.hackerrank.com/challenges/itertools-combinations-with-replacement/problem

from itertools import combinations_with_replacement as cr

input_value = list(input().strip().split())
for i in list(cr(sorted(input_value[0]), int(input_value[1]))):
    print(''.join(i))