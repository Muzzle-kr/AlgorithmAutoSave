def gcd(a, b):
    if a % b == 0:
        return b
    return gcd(b, a % b)

a, b = map(int, input().split())
c, d = map(int, input().split())

A = a * d
B = b * d
C = c * b
D = b * d

E = A + C
F = gcd(E, D)
E = E // F
D = D // F

print(E, D)