N = int(input())

maxScore = 0
for _ in range(N):
    a, d, g = map(int, input().split())
    
    if a == (d + g):
        maxScore = max(maxScore, a * (d + g) * 2)
    else:
        maxScore = max(maxScore, a * (d + g))

print(maxScore)