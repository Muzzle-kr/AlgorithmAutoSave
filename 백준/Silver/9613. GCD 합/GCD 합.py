def gcd(a, b):
    if a % b == 0:
        return b
    return gcd(b, a % b)

for _ in range(int(input())):
    arr = list(map(int, input().split()))
    n = arr[0]
    arr = arr[1:]
    
    total = 0
    
    for i in range(n):
        for j in range(i + 1, n):
            total += gcd(arr[i], arr[j])
    
    print(total)