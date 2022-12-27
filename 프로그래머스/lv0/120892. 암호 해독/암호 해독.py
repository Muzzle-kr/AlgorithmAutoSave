def solution(cipher, code):
    answer = ''
    
    for idx, c in enumerate(cipher):
        if (idx + 1) % code == 0:
            answer += c
    return answer