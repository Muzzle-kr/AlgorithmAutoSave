roll = [0 for i in range(30)]

for _ in range(28):
    i = int(input())
    roll[i-1] = 1

for idx, i in enumerate(roll):
    if i == 0:
        print(idx + 1)