prime_number, seed, x1, x2 = map(int, input().split())

for i in range(prime_number):
    
    for j in range(prime_number):
        if (i * seed + j) % prime_number == x1 and (i * x1 + j) % prime_number == x2:
            print(i, j)
            exit()