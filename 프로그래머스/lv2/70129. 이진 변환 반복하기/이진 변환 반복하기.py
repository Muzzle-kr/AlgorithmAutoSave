def convertToBinary(num):
    result = ""
    
    while num > 1:
        result = str(num % 2) + result
        num = num // 2
    
    result = str(num) + result
    return result

def solution(s):
    answer = [0, 0] # [이진변환횟수, 제거된 0의 갯수]
    count = 0
    while s != "1":
        if count == 8:
            break
        string = ""
        for i in s:
            if i == "0":
                answer[1] += 1
            else:
                string += i
        
        length = len(string)
        s = convertToBinary(length)
        answer[0] += 1
        count += 1
        # print(f'answer:{answer}, string: {string}, length: {length}, s: {s}')
        
    return answer