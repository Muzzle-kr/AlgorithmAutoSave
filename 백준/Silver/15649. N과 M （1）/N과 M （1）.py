from itertools import permutations

N, M = map(int, input().split())

arr = [i for i in range(1, N + 1)]
permutation = list(permutations(arr, M))

for i in permutation:
    print(*i)