from collections import Counter

for i in range(int(input())):
    a, b = input().split()
    
    # print(Counter(a), Counter(b))
    if Counter(a) == Counter(b):
        print("Possible")
    else:
        print("Impossible")