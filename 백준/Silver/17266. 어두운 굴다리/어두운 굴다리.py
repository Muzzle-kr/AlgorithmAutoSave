import sys
input = sys.stdin.readline

N = int(input())
M = int(input())

streetlights = list(map(int, input().split()))
min_height = streetlights[0]

for i in range(1, M):
    diff = (streetlights[i] - streetlights[i-1])
    
    if diff % 2 == 0:
        diff //= 2
    else:
        diff = diff // 2 + 1
    
    min_height = max(min_height, diff)

min_height = max(min_height, N - streetlights[-1])

print(min_height)