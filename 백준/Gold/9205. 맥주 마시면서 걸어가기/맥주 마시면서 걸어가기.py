from collections import deque

def distance(x1, y1, x2, y2):
    return abs(x1-x2) + abs(y1-y2)

def bfs(x, y):
    global end_x, end_y
    deq = deque([(x, y)])
    visited = set()

    while deq:
        x, y = deq.popleft()
        if distance(x, y, end_x, end_y) <= 1000:
            return True
        for i in range(s):
            store_x, store_y = store[i]
            if (store_x, store_y) not in visited:
                if distance(x, y, store_x, store_y) <= 1000:
                    visited.add((store_x, store_y))
                    deq.append((store_x, store_y))
    return False


for _ in range(int(input())):
    s = int(input())
    start_x, start_y = map(int, input().split())
    store = [tuple(map(int, input().split())) for _ in range(s)]
    end_x, end_y = map(int, input().split())
    check = bfs(start_x, start_y)
    print('happy' if check else 'sad')