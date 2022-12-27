def solution(hp):
    answer = 0
    # print(f'hp: {hp}, answer: {answer}')
    if hp >= 5:
        answer += (hp // 5)
        hp %= 5        
    # print(f'hp: {hp}, answer: {answer}')
    if hp >= 3:
        answer += (hp // 3)
        hp %= 3
    # print(f'hp: {hp}, answer: {answer}')
    if hp >= 1:
        answer += (hp // 1)
        hp %= 1
    # print(f'hp: {hp}, answer: {answer}')
    return answer