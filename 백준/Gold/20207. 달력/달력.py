N = int(input())
appointments = [0] * 366

for _ in range(N):
    s, e = map(int, input().split())

    for i in range(s, e + 1):
        appointments[i] += 1

length = 0
height = 0
ans = 0

for i in range(1, 366):
    if appointments[i] >= 1:
        length += 1
        height = max(height, appointments[i])
    else:
        if length != 0:
            ans += length * max(height, 1)
            
        length = 0
        height = 0

# 한 번 더 계산해주기
if length != 0:
    ans += length * max(height, 1)
print(ans)