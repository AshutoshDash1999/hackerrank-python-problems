# problem-link = https://www.hackerrank.com/challenges/collections-counter/problem

from collections import Counter as c

X = int(input())
shoe_size_list = list(map(int, input().strip().split()))
N = int(input())
total_money = 0

for i in range(N):
    input_value = list(map(int, input().strip().split()))

    if input_value[0] in shoe_size_list:
        total_money = total_money + input_value[1]
        shoe_size_list.remove(input_value[0])

    else:
        total_money = total_money + 0

print(total_money)
