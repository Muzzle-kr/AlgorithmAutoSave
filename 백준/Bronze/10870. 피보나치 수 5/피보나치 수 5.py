N = int(input())
fibonacci = [0, 1]

for i in range(2, 21):
    fibonacci.append(fibonacci[i - 1] + fibonacci[i - 2])

print(fibonacci[N])
