# problem-link = https://www.hackerrank.com/challenges/np-polynomials/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge

import numpy as np
coefficients_p = list(map(float, input().strip().split()))
x = int(input())
print(np.polyval(coefficients_p, x))