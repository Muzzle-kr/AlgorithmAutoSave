import sys
input = sys.stdin.readline
from collections import defaultdict

m, n = map(int, input().split())
universe = defaultdict(int)

for _ in range(m):
    arr = list(map(int, input().split()))
    sorted_arr = sorted(list(set(arr)))
    dict_arr = {sorted_arr[i]: i for i in range(len(sorted_arr))}
    c = tuple([dict_arr[i] for i in arr])
    universe[c] += 1

sum = 0
for i in universe.values():
    sum += i * (i - 1) // 2

print(sum)