from collections import defaultdict
t = int(input())

for _ in range(t):
    a, b = input().split()
    
    if len(a) != len(b):
        print(f'{a} & {b} are NOT anagrams.')
    else:
        dic_a = defaultdict(int)
        dic_b = defaultdict(int)
        for aa in a:
            dic_a[aa] += 1
        
        for bb in b:
            dic_b[bb] += 1
        
        if dic_a == dic_b:
            print(f'{a} & {b} are anagrams.')
        else:
            print(f'{a} & {b} are NOT anagrams.')