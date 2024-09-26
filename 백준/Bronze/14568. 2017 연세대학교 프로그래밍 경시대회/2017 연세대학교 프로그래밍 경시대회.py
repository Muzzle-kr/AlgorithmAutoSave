candy = int(input())
count = 0

for i in range(1, candy - 1):
    for j in range(1, candy - 1):
        if i >= j + 2:
            for k in range(1, candy - 1):
                if k % 2 == 0 and i + j + k == candy:
                    count += 1

print(count)