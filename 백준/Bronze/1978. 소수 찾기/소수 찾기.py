def isPrime(n):
    if n == 1:
        return False

    for i in range(2, int(n**0.5)+1):
        if (n % i) == 0:
            return False

    return True

N = int(input())
numbers = list(map(int, input().split()))

total = 0
for number in numbers:
    total += 1 if isPrime(number) else 0
print(total)
