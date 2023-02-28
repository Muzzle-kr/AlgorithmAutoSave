import bisect

n = int(input())
v = []
for i in range(n):
    a, b = map(int, input().split())
    v.append((a, b))

v.sort()
left = [-1] * n
right = [-1] * n


def find_left(here):
    if left[here] != -1:
        return left[here]

    a, b = v[here]
    t = bisect.bisect_left(v, (a-b, -1))
    ret = t
    for t in range(t, here):
        ret = min(ret, find_left(t))
    left[here] = ret
    return ret


def find_right(here):
    if right[here] != -1:
        return right[here]

    a, b = v[here]
    t = bisect.bisect_right(v, (a+b, float('inf')))
    ret = t-1
    for t in range(here+1, t):
        ret = max(ret, find_right(t))
    right[here] = ret
    return ret


for i in range(n):
    find_left(i)
    find_right(i)

dp = [float('inf')] * n
dp[0] = 1

for i in range(n):
    dp[i] = min(dp[i], 1 + (dp[left[i]-1] if left[i]-1 >= 0 else 0))
    for j in range(i):
        if right[j] >= i:
            dp[i] = min(dp[i], 1 + (dp[j-1] if j-1 >= 0 else 0))

print(dp[n-1])