import sys
from fractions import Fraction
input = sys.stdin.readline
fac_arr = [0, 1]

def factorial():
    for i in range(2, 101):
        fac_arr.append(fac_arr[i-1] * i)

def solution():
    n, m = map(int, input().split())
    return Fraction(fac_arr[n], (fac_arr[m] * fac_arr[n-m]))
    
factorial()
print(solution())