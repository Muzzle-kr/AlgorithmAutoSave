import sys
input = sys.stdin.readline

    
def solution():
    N = int(input())
    stack = list()
    
    for _ in range(N):
        num_list = list(map(int, input().split()))
        if num_list[0] == 1:
            n = num_list[1]
            stack.append(n)
        elif num_list[0] == 2:
            print(-1 if len(stack) == 0 else stack.pop())
        elif num_list[0] == 3:
            print(len(stack))
        elif num_list[0] == 4:
            print(1 if len(stack) == 0 else 0)
        elif num_list[0] == 5:
            print(-1 if len(stack) == 0 else stack[-1])
solution()