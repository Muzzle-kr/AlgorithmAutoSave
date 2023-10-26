n = int(input())
arr = list(map(int, input().split()))

point = arr[0]
result = []

def gcd(a, b):
    if a % b == 0:
        return b
    return gcd(b, a % b)

for i in range(1, len(arr)):
    GCD = gcd(arr[i], point)
    print(str(point//GCD) + '/' + str(arr[i]//GCD))