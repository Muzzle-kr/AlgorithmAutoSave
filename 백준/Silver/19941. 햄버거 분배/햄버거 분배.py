# 가장 왼쪽부터 먹는다.
import sys
input = sys.stdin.readline
N, K = map(int, input().split())
lines = list(input())
ans = 0

for i in range(N):
    if lines[i] == 'P':
        for j in range(max(0, i-K), min(N, i+K+1)):
            if lines[j] == 'H':
                lines[j] = 'X'
                ans += 1
                break
print(ans)