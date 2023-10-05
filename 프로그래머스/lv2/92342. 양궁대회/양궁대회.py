# 최대 큰 점수로 이기는 방법 -> 0을 많이 먹고, 1을 많이 먹는 방법
import heapq as hq
import sys
import copy
sys.setrecursionlimit(10**6)
# 완탐으로 이기는 경우를 힙에 넣고, 가장 큰 점수로 이기는 경우를 출력

def apply_weight(arr):
    total = 0
    for i in range(11):
        total += (10**i) * arr[i]
    return total

def get_score_diff(apeach, lion):
    apeach_score = 0
    lion_score = 0
    
    for i in range(11):
        if lion[i] > apeach[i]:
            lion_score += 10 - i
            
        elif lion[i] <= apeach[i]:
            if lion[i] == 0 and apeach[i] == 0:
                continue
            apeach_score += 10 - i  
    return lion_score - apeach_score

def check_lion_win(apeach, lion):
    return get_score_diff(apeach, lion) > 0


def bt(idx, arrow, apeach, lion, queue):
    
    # 과녁을 다 쏜 경우
    if idx >= 11:
        score_diff = get_score_diff(apeach, lion)
        
        # 라이언이 이기는 경우
        if score_diff > 0:
            applied_weight_total = apply_weight(lion)
            # 우선순위 큐에 넣기
            hq.heappush(queue, [-score_diff, -applied_weight_total, copy.deepcopy(lion)])
            
        return
    
    # 마지막 과녁에서 화살이 남는 경우 처리
    if idx == 10:
        lion[idx] = arrow
        bt(idx+1, 0, apeach, lion, queue)
        lion[idx] = 0
        return
    
    # 남은 화살이 없는 경우     
    if arrow == 0:
        bt(11, arrow, apeach, lion, queue)
    
    # 라이언이 해당 과녁을 맞추는 경우
    if arrow >= apeach[idx] + 1: 
        lion[idx] += apeach[idx] + 1
        bt(idx+1, arrow - (apeach[idx] + 1), apeach, lion, queue)
        
        # 복원
        lion[idx] -= apeach[idx] + 1
        
    # 라이언이 해당 과녁을 스킵하는 경우
    bt(idx+1, arrow, apeach, lion, queue)
    
    
        
def solution(n, info):
    lion = [0] * 11
    queue = []
    # 백트래킹 시작 
    bt(0, n, info, lion, queue)

    
    if len(queue) == 0:
        return [-1]
    else:
        return hq.heappop(queue)[2]