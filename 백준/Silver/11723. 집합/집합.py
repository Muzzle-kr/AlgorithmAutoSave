import sys
input = sys.stdin.readline

arr = [0] * 21

for _ in range(int(input())):
    order = input().split()
    
    if order[0] == "all" or order[0] == "empty":
        for i in range(1,21):
            arr[i] = 1 if order[0] == "all" else 0
    else:
        command = order[0]
        num = int(order[1])
        
        if command == "add":
            if arr[num] == 0:
                arr[num] = 1
        
        elif command == "remove":
            if arr[num] == 1:
                arr[num] = 0
    
        elif command == "check":
            if arr[num] == 1:
                print(1)
            else:
                print(0)
    
        elif command == "toggle":
            if arr[num] == 1:
                arr[num] = 0
            else:
                arr[num] = 1
