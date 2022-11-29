def solution(num, total):
    answer = []
    
    share = total // num
    if num % 2 == 0:
        for i in range(share - (num // 2) + 1, share + (num // 2) + 1):
            answer.append(i)
    else:
        for i in range(share - (num // 2), share + (num // 2) + 1):
            answer.append(i)
    return answer