import sys

input = sys.stdin.readline
string = input().strip()
bomb = input().strip()

# 문자를 돌면서 폭발 문자열이 있는 지 찾는다.
# 폭발 문자열이 있으면 그 문자열을 제거하고 다시 폭발 문자열이 있는 지 찾는다.
# 반복!

stack = []
bomb_length = (len(bomb))

for i in range(len(string)):
    stack.append(string[i])
    
    if "".join(stack[-bomb_length:]) == bomb:
        for _ in range(bomb_length):
            stack.pop()
    
    
    
    
if stack:
    print("".join(stack))
else:
    print("FRULA")