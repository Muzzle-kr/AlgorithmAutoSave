def solution(n, times):
    answer = 0
    # 사용 중이면 1, 사용 중이 아니면 0
    min_time = times[0]
    max_time = times[0] * n
    
    while True:
        mid_time = (min_time + max_time) // 2
        count = 0
        
        for time in times:
            count += mid_time // time
        
        if count >= n:
            answer = mid_time
            max_time = mid_time - 1
        else:
            min_time = mid_time + 1
            
        if min_time > max_time:
            break
    return answer 