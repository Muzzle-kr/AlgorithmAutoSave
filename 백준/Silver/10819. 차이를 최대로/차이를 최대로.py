n = int(input())
from itertools import permutations
answer = 0
arr = list(map(int, input().split()))
combi = list(permutations(arr, n))

for c in combi:
    total = 0
    for i in range(n-1):
        total += abs(c[i]-c[i+1])
        answer = max(answer, total)

print(answer)