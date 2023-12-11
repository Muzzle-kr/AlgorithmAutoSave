from itertools import permutations
n = int(input())
k = int(input())

arr = [input() for _ in range(n)]

combination = set(["".join(p) for p in permutations(arr, k)])
print(len(combination))