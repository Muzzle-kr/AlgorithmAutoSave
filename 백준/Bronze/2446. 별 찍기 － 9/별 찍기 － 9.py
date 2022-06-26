repeat = int(input())

time = 0
while time < 2:
    max = repeat
    if time == 0:
        for i in range(repeat, 0, -1):
            print(" " * (max - i), end="")
            print("*" * (i * 2 -1))
    elif time == 1:
        for i in range(2, repeat + 1):
            print(" " * (max - i), end="")
            print("*" * (i * 2 -1))
    time += 1    