# problem-link = https://www.hackerrank.com/challenges/itertools-product/problem
# the problem is self explainatory from the above link


from itertools import product
A = list(map(int, input().split()))
B = list(map(int, input().split()))
product = list(product(A,B))
final = " ".join(map(str, product))
print(final)
