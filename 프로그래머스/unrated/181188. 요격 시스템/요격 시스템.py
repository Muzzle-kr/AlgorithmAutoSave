def solution(targets):
    answer = 0
    targets.sort(key=lambda x: (x[0], -x[1]))
    first_idx = 0
    last_idx = 0
    
    for a, b in targets:
        # 새로운 끝점이 기존의 끝점보다 작다면 요격 가능
        if b < last_idx:
            continue
        else:
            if a < last_idx:
                first_idx = a
            else:
                last_idx = b
                first_idx = a
                answer += 1
    return answer