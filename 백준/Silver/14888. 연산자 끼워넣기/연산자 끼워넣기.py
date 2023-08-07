import sys
from itertools import permutations

input = sys.stdin.readline
N = int(input())
arr = list(map(int, input().split()))
plus, minus, mul, div = map(int, input().split())
total = plus + minus + mul + div
signs = (['+']*plus) + (['-']*minus) + (['*']*mul) + (['//']*div)
permutation = set(permutations(signs, total))

min = sys.maxsize
max = -sys.maxsize

for p in permutation:
    t = 0
    n = arr[0]
    
    for i in range(1, N):
        if p[i-1] == "//":
            if n < 0:
                n = -(-n // arr[i])
            else:
                n //= arr[i]
        else:
            n = eval(str(n) + p[i-1] + str(arr[i]))

    if n < min:
        min = n
    
    if n > max:
        max = n

print(max)
print(min)