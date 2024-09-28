a, b = map(int, input().split())

def _gcd(a, b):
    while a % b != 0:
        tmp = a % b
        a = b
        b = tmp
    return b

gcd = _gcd(a, b)
lcm = a * b // gcd
print(gcd)
print(lcm)