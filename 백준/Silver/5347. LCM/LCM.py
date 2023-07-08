def get_gcd(a, b):
    if a % b == 0:
        return b
    else:
        return get_gcd(b, a%b)
    
for _ in range(int(input())):
    a, b = map(int, input().split())
    gcd = get_gcd(a, b)
    
    print(a*b//gcd)
    