# problem-link = https://www.hackerrank.com/challenges/text-wrap/problem

import textwrap
text = input()
width = int(input())
for i in textwrap.wrap(text, width):
    print(i)