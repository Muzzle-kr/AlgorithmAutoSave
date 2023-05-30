t = int(input())

for _ in range(t):
    ans = 0
    
    n, m = map(int, input().split())
    for i in range(1, n-1):
        for j in range(i+1, n):
            result = ((i**2)+(j**2)+m)/(i*j)
            if result == int(result):
                ans += 1
                
    print(ans)   