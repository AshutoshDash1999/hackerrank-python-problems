# problem link = https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem
# as the scores repeat so i converted them to set as
# values are not repeated in sets then it is converted into list
# where we have sort function. The second largest value is the runner up score


n = int(input())
A = input()
list_n = list(map(int, A.split()))
if len(list_n) == n:
    list_n.sort()
    list_set = list(set(list_n))
    sorted_list = list_set.sort()
    print(list_set[-2])
else:
    print("Something is wrong")
