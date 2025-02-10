answer = 0
total = 0

for i in range(10):
    a, b = map(int, input().split())

    total -= a
    total += b

    answer = max(answer, total)

print(answer)
