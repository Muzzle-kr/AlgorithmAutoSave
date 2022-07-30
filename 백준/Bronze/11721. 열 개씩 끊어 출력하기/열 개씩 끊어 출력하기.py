string = input()
length = len(string)
for i in range(length // 10 + 1):
    print(string[10 * i: 10 * (i + 1)])