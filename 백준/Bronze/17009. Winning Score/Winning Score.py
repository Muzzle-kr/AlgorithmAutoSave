apple = 0
banana = 0

apple += int(input()) * 3
apple += int(input()) * 2
apple += int(input()) * 1
banana += int(input()) * 3
banana += int(input()) * 2
banana += int(input()) * 1

if apple > banana:
    print("A")
elif apple < banana:
    print("B")
else:
    print("T")