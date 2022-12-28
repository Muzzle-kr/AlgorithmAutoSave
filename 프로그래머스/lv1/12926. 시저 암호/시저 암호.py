def solution(s, n):
    answer = ''
    
    for i in s:
        if i == " ":
            answer += i
            continue
        
        num = ord(i)
        
        if num < 97:
            # 90을 넘으면 65부터 시작
            if num + n > 90:
                answer += chr((num + n) % 90 + 64)
            else:
                answer += chr(num + n)
        else:
            # 122를 넘으면 97부터 시작 
            if num + n > 122:
                answer += chr((num + n) % 122 + 96)
            else:
                answer += chr(num + n)
    
    return answer