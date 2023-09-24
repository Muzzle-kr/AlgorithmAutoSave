def get_gcd(a, b):
    if a % b == 0:
        return b
    return get_gcd(b, a % b)

a, b = map(int, input().split())
gcd = get_gcd(a, b)

print(a * b // gcd)