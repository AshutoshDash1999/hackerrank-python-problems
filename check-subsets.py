# problem link = https://www.hackerrank.com/challenges/py-check-subset/problem
# more info on set thoery = https://www.britannica.com/science/set-theory
# to check if A is subset of B, we have to check if all
# the elements in A is present in B.
# in other words check if intersection of A and B == A


T = int(input())
for i in range(T):
    A_num = input()
    A_input = input()
    A_set = set(map(int, A_input.split()))
    B_num = input()
    B_input = input()
    B_set = set(map(int, B_input.split()))
    intersected = B_set.intersection(A_set)
    if intersected == A_set:
        print(True)
    else:
        print(False)