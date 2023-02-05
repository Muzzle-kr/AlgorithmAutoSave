
for i in range(int(input())):
    n, m = map(int, input().split())
    
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    a.sort()
    b.sort()
    
    count = 0
    for i in a:
        for j in b:
            if i > j:
                count += 1
            else:
                break
    print(count)