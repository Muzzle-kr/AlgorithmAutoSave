from itertools import permutations
arr = [i for i in range(1, int(input())+1)]
permutation = list(permutations(arr, len(arr)))

for i in permutation:
    print(*i)