from itertools import combinations

arr = [int(input()) for i in range(9)]

combination = combinations(arr, 7)

for combi in combination:
    if sum(combi) == 100:
        for c in sorted(combi):
            print(c)
        break
