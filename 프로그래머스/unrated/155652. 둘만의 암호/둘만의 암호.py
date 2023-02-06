def solution(s, skip, index):
    answer = ''
    skipArr = [ord(i) for i in skip]
    
    for w in s:
        unicodeNum = ord(w)
        

        for _ in range(index):
            unicodeNum += 1
            
            if unicodeNum > 122:
                unicodeNum = 97 + (unicodeNum - 123)
                        
            while unicodeNum in skipArr:
                unicodeNum += 1
                if unicodeNum > 122:
                    unicodeNum = 97 + (unicodeNum - 123)

        answer += chr(unicodeNum)
    return answer