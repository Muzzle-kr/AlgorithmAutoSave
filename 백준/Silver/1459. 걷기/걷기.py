import heapq as hq
x, y, w, s = map(int, input().split())
result = 0

# 평행 이동
r1 = (x + y) * w

# 대각선 이동
if (x + y) % 2 == 0:
    r2 = max(x, y) * s
else:
    r2 = (max(x, y) - 1) * s + w

# 평행이동 + 대각선 이동
r3 = (min(x, y) * s) + (abs(x-y) * w)

print(min(r1, r2, r3))