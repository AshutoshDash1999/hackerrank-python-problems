# problem-link = https://www.hackerrank.com/challenges/py-set-symmetric-difference-operation/problem


n = input()
n_roll = input()
n_set = set(map(int, n_roll.split()))

b = input()
b_roll = input()
b_set = set(map(int, b_roll.split()))

not_both = n_set.symmetric_difference(b_set)
print(len(not_both))
