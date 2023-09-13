import sys
input = sys.stdin.readline
N, M = map(int, input().rstrip().split())

# 가장 먼저 입력된 칭호 하나!
title_power = []

for _ in range(N):
    title, power = input().rstrip().split()
    title_power.append((title, int(power)))

for _ in range(M):
    p = int(input())
    
    title = ''
    left = 0
    right = len(title_power) - 1
    
    while left <= right:
        mid = (left + right) // 2    
        if title_power[mid][1] < p:
            left = mid + 1
        else:
            right = mid - 1
            title = title_power[mid][0]
    print(title)
