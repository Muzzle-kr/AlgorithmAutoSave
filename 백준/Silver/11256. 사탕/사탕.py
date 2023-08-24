for _ in range(int(input())):
    N, M = map(int, input().split())
    boxes = sorted([list(map(int,input().split())) for _ in range(M)], key=lambda x: x[0]*x[1], reverse=True)
    ans = 0
    
    for a, b in boxes:
        box_size = a * b

        N -= box_size
        ans += 1
        if N <= 0:
            break
    print(ans)
        
    