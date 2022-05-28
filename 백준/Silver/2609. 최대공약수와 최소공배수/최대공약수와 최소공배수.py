a, b = map(int, input().split())

def gcd(a, b):
    if a % b == 0:
        return b
    else: 
        return gcd(b, a % b)
        
    
def lcm(a, b):
    value = gcd(a, b)
    return int(a * b / value)

print(gcd(a, b))
print(lcm(a, b))