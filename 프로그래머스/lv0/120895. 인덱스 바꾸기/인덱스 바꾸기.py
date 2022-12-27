def solution(my_string, num1, num2):
    answer = list(my_string)
    
    tmp = answer[num1]
    answer[num1] = answer[num2]
    answer[num2] = tmp
    return "".join(answer)