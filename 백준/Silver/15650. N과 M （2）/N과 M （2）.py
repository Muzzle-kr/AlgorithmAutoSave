from itertools import combinations

N, M = map(int, input().split())

arr = [i for i in range(1, N + 1)]
combination = list(combinations(arr, M))

for i in combination:
    print(*i)