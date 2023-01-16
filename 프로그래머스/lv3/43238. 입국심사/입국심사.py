def solution(n, times):
    answer = 0
    min_time = times[0]
    max_time = times[0] * n

    while True:
        mid_time = (min_time + max_time) // 2
        count = 0
        
        for t in times:
            count += mid_time // t
        
        if count < n:
            min_time = mid_time + 1
        else:
            max_time = mid_time - 1
        
        if min_time > max_time:
            answer = min_time
            break
    return answer