s = int(input())
compare = 0

for i in range(1, 4294967296):
    compare += i
    if compare > s:
        print(i-1)
        break