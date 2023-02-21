from collections import deque
import math
def solution(storey):
    

    answer = 0
    
    q = deque()
    q.append((storey, 0))
    
    while q:
        n, count = q.popleft()
        n = str(n)
        length = len(n)
        
        if n == '0':
            return count
        
        # 반올림해서 해당 숫자에서 제외 시킨다.
        
        for i in range(len(n)-1, -1, -1):
            
            if n[i] == '0':
                continue
            
            # round 사사오입 원칙으로 임의로 5를 4로 바꿔서 반올림
            if n[i] == '5':
                n = n[:i] + '4' + n[i+1:]
                count += 1
                
            rounded = round(int(n), -((length - i)))
            diff = abs(rounded - int(n)) // (10 ** (length - i - 1))
            
            if i == 0:
                return count + diff
                # q.append(('0', count + diff))                
            
            q.append((rounded, count + diff))
            break