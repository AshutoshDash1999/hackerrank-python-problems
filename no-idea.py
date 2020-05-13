# problem-link = https://www.hackerrank.com/challenges/no-idea/problem
# explanation is given in the above link


happiness = 0
def convert_input_to_list(values):
    converted_list = list(map(int, values.split()))
    return converted_list

def convert_input_to_setlist(values):
    converted_setlist = list(set(list(map(int, values.split()))))
    return converted_setlist

first_input = convert_input_to_setlist(input())
second_input = convert_input_to_setlist(input())
A = convert_input_to_setlist(input())
B = convert_input_to_setlist(input())

for i in second_input:
    if i in A:
        happiness = happiness+1

for i in second_input:
    if i in B:
        happiness = happiness - 1

print(happiness)
