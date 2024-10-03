string = input()

for i in range(len(string)):
    if string[i:] == string[i:][::-1]:
        print(len(string) + i)
        break