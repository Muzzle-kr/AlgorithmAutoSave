import sys
input = sys.stdin.readline

n, k = map(int, input().split())
numbers = input().rstrip()
stack = []

for number in numbers:
    # 스택이 비어있지 않고, k가 0보다 크고, 스택의 마지막 숫자가 현재 숫자보다 작은 경우
    while stack and stack[-1] < number and k > 0:
        stack.pop()
        k -= 1
    stack.append(number)

if k != 0:
    print("".join(stack[:-k]))
else:
    print("".join(stack))