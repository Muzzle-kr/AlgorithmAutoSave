repeat = int(input())

setting = [0, 1, 0, 0]

for _ in range(repeat):
    x, y = map(int, input().split())
    tmp = 0
    tmp = setting[x]
    setting[x] = setting[y]
    setting[y] = tmp


for idx, i in enumerate(setting):
    if i == 1:
        print(idx)