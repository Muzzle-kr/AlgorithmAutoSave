def solution(array):
    answer = [0, 0]
    
    for idx, i in enumerate(array):
        if i > answer[0]:
            answer[0] = i
            answer[1] = idx
    return answer