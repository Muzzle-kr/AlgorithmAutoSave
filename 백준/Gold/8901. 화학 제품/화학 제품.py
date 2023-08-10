T = int(input())
for _ in range(T):
    a, b, c = map(int, input().split())
    abP, bcP, caP = map(int, input().split())
    
    maxPrice = 0
    
    
    for abNum in range(min(a, b) + 1):
        bcNum = min(c, b - abNum)
        caNum = min(c - bcNum, a - abNum)
        
        maxPrice = max(maxPrice, abNum * abP + bcNum * bcP + caNum * caP)
        
        caNum = min(a - abNum, c)
        bcNum = min(b - abNum, c - caNum)
        
        maxPrice = max(maxPrice, abNum * abP + bcNum * bcP + caNum * caP)
    
    print(maxPrice)