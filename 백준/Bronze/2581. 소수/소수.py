def isPrime(n):
    if n == 1:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True


n = int(input())
m = int(input())

total = 0
min_prime = 0

for i in range(n, m + 1):
    if isPrime(i):
        total += i
        if min_prime == 0:
            min_prime = i

if total == 0:
    print(-1)
else:
    print(total)
    print(min_prime)
