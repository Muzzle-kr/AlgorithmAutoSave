D1, D2 = map(int, input().split())

mp1 = {}
ans = 0

def gcd(a, b):
    return b if a % b == 0 else gcd(b, a % b)

for i in range(D1, D2 + 1):
    mp2 = {}
    for j in range(1, i):
        g = gcd(i, j)
        if mp1.get(i // g):
            continue
        ans += 1
        mp2[i // g] = 1

    for p in mp2:
        mp1[p] = 1

print(ans + 1)