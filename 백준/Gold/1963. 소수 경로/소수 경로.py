from collections import deque
import sys

def bfs():
    q = deque()
    q.append((str(a), 0))
    visited = [False] * 10001
    visited[a] = True
    
    while q:
        number, cnt = q.popleft()
        
        if int(number) == b:
            return cnt
        
        
        for i in range(4):
            for j in range(10):
                new_number = int(number[:i] + str(j) + number[i+1:])
                if new_number >= 1000 and is_prime[new_number] and not visited[new_number]:
                    visited[new_number] = True
                    q.append((str(new_number), cnt+1))
        
    return -1
input = sys.stdin.readline
T = int(input())
is_prime = [True] * 10001

for i in range(2, 10001):
    for k in range(2*i, 10001, i):
        is_prime[k] = False

for _ in range(T):
    a, b = map(int, input().split())
    result = bfs()
    
    if result == -1:
        print('Impossible')
    else:
        print(result)