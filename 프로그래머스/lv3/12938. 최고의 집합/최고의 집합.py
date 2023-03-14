import sys
import math
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
# 계속 나누기
def solution(n, s):
    
    answer = []
    while len(answer) < n:
        if len(answer) == n - 1:
            answer.append(s)
            break
        

        quota = s // (n - len(answer))
        if quota == 0:
            answer = [-1]
            break
        s -= quota
        answer.append(quota)
        
    return answer