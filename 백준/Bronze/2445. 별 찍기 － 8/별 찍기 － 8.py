repeat = int(input())

time = 0
while time < 2:
    if time == 0:
        for i in range(1, repeat + 1):
            max = repeat * 2
            print("*" * i, end="")
            print(" " * (max - i * 2), end="")
            print("*" * i)
    elif time == 1:
        for i in range(repeat-1, 0, -1):
            max = repeat * 2
            print("*" * i, end="")
            print(" " * (max - i * 2), end="")
            print("*" * i)
    time += 1    