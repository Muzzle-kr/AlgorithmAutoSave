import sys
import heapq as hq
input = sys.stdin.readline

N = int(input())

for _ in range(N):
    M = int(input())
    
    pool = []
    for i in range(M):
        pool.append(list(map(int, input().split())))
    # 첫번째 성적순 정리
    
    pool = sorted(pool, key=lambda x: x[0]) 
    
    dropout = 1
    order = 0
    lastDropout = 0
    for i in range(1, M):
        currentApplicant = pool[i]
        comparison = pool[lastDropout]
        # print(f'i: {i}, currentApplicant: {currentApplicant}, comparison: {comparison}')
        # 면접 심사 순위가 더 떨어지는 사람을 탈락시킴
        if pool[i][1] < pool[lastDropout][1]:
            # print(f'살아남은자: {i}')
            # 탈락자 추가
            dropout += 1
            # 마지막 탈락자 index 변경
            lastDropout = i
        
    print(dropout)