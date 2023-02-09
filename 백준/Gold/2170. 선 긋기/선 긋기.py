import sys
import heapq as hq

input = sys.stdin.readline
n = int(input())
paper = []
answer = 0

for i in range(n):
    paper.append(tuple(map(int, input().split()))) 
    
paper.sort()                                                                                                                                                                             

start = paper[0][0]
end = paper[0][1]


for i in range(1, n):
    
    # print(f'paper[{i}] = {paper[i]}')
    if paper[i][0] <= end:
        end = max(end, paper[i][1])
    
    elif paper[i][0] > end:
        answer += end - start
        start = paper[i][0]
        end = paper[i][1]
    

answer += end - start
print(answer)