def solution(box, n):
    answer = 1
    
    
    for b in box:
        # print(f'b: {b}')
        max = 0
        for i in range(1, b + 1):
            if i % n == 0:
                if i > max:
                    max = i
            # print(f'max: {max}')
        answer *= max
    
    answer = int(answer / (n ** 3))
    return answer