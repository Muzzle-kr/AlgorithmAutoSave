from itertools import combinations

while True:
    a = list(map(int, input().split()))
    
    if len(a) == 1:
        break
    
    length = a[0]
    gather = a[1:]
    
    for c in combinations(gather, 6):
        print(*c)

    print()