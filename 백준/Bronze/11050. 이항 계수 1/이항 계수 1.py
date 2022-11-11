from itertools import combinations
import sys

N, K = map(int, input().split())

combination = combinations(range(N), K)

result=0
for c in combination:
    result+=1

print(result)