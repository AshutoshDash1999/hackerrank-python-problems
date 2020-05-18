# problem-link = https://www.hackerrank.com/challenges/itertools-permutations/problem

from itertools import permutations as p
input_value = list(input().strip().split())
perm_list = list(p(sorted(input_value[0]), int(input_value[1])))
for i in perm_list:
    print(''.join(i))