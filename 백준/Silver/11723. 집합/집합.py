import sys
input = sys.stdin.readline
N = int(input())
dict = {}

for _ in range(N):
    operation = list(input().split())
    order = operation[0]
    
    if order == "add":
        dict[int(operation[1])] = 1
    elif order == "remove":
        if int(operation[1]) in dict:
            del dict[int(operation[1])]
    elif order == "check":
        if int(operation[1]) in dict:
            print(1)
        else:
            print(0)
    elif order == "toggle":
        if int(operation[1]) in dict:
            del dict[int(operation[1])]
        else:
            dict[int(operation[1])] = 1
    elif order == "all":
        dict = {i:1 for i in range(1,21)}
    else:
        dict = {}
        