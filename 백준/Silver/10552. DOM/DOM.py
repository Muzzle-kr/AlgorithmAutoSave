from collections import defaultdict, deque
import sys

def bfs(s):
    q = deque()
    q.append((s, 0))
    total_cnt = 0
    
    while q:
        x, cnt = q.popleft()
        
        if total_cnt > n*2:
            return -1
        
        if x not in hate_dict.keys():
            return cnt
        
        # 여러 명일 경우 막내부터 일어섬
        idx = hate_dict[x][0]
        q.append((like_arr[idx], cnt+1))
        total_cnt += 1
        
    return -1

input = sys.stdin.readline
n, m, p = map(int, input().split())
like_arr = []
hate_arr = []
like_dict = defaultdict(list)
hate_dict = defaultdict(list)

for i in range(n):
    liked, hated = map(int, input().split())
    
    like_arr.append(liked)
    hate_arr.append(hated)
    
    like_dict[liked].append(i)
    hate_dict[hated].append(i)

print(bfs(p))