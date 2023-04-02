n = int(input())

minX = int(1e9)
maxX = int(-1e9)
minY = int(1e9)
maxY = int(-1e9)

for _ in range(n):
    x, y = map(int, input().split())
    
    minX = min(minX, x)
    maxX = max(maxX, x)
    minY = min(minY, y)
    maxY = max(maxY, y)

print((maxX - minX) * (maxY - minY))