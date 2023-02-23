import heapq as hq

def solution(n, k, enemy):
    answer = 0
    # 남은 병사 수보다 적들이 많을 때 사용
    enemyArr = []
    
    for idx, e in enumerate(enemy):
        
        n -= e
        hq.heappush(enemyArr, (-e, e))
        
        if n < 0:
            if k > 0:
                invincible = hq.heappop(enemyArr)[1]
                n += invincible
                k -= 1
            else:
                break
        answer += 1

    return answer