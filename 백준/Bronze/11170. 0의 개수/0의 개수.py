for _ in range(int(input())):
    N, M = map(int, input().split())
    
    count = 0
    for i in range(N, M + 1):
        for j in str(i):
            if j == '0':
                count += 1
    print(count)