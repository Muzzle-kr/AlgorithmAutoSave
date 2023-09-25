def solution(sequence, k):
    answer = []
    length = len(sequence)
    sum_arr = [sequence[0]]
    
    for i in range(1, length):
        sum_arr.append(sum_arr[i-1] + sequence[i])
    
    left = -1
    right = 0
    
    while right < length and left < length:
        total = 0
        if left > -1:
            total = sum_arr[right] - sum_arr[left]
        else:
            total = sum_arr[right]    
        
        # print(f'left: {left}, right: {right}, total: {total}')
        
        if total > k:
            left += 1
        elif total < k:
            right += 1
        else:
            answer.append([left + 1, right])
            left += 1
            right += 1
            
    answer.sort(key=lambda x: abs(x[0]-x[1]))
    return answer[0]