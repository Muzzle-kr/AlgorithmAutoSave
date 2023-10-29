from collections import deque
N = int(input())

queue = deque()

for i in range(1, N+1):
    queue.append(i)

result = []

while len(queue) > 1:
    result.append(queue.popleft())
    queue.append(queue.popleft())

result.append(queue.pop())
print(*result)