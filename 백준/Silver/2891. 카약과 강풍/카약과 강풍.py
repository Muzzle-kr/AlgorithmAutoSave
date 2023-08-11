N, S, R = map(int, input().split())
damaged = list(map(int, input().split()))
reserve = list(map(int, input().split()))
damaged.sort()

ans = 0

self_fix = []

for i in range(len(damaged)):
    if damaged[i] in reserve:
        reserve.remove(damaged[i])
        self_fix.append(damaged[i])
        continue

for i in self_fix:
    damaged.remove(i)


for i in range(len(damaged)):    
    if damaged[i] - 1 in reserve:
        reserve.remove(damaged[i] - 1)
        continue

    if damaged[i] + 1 in reserve:
        reserve.remove(damaged[i] + 1)
        continue

    ans += 1

print(ans)