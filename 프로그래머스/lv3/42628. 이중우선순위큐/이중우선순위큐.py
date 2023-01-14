import heapq as hq

def solution(operations):
    
    answer = []
    for i in range(len(operations)):
        command, number = operations[i].split()
        number = int(number)
        # print(f'현재 Answer: {answer}, 명령어: {command}, 숫자: {number}')    
        if command == "I":
            hq.heappush(answer, number)
        else:
            if answer:
                if number < 0:
                    hq.heappop(answer) 
                else:
                    tmp = []
                    
                    while answer:
                        tmp.append(hq.heappop(answer))
                    
                    answer = tmp[:-1]
                
                
            
    # print(f'최종 Answer: {answer}')    
    if len(answer) == 0:
        return [0, 0]
    else:
        tmp = []
        
        while answer:
            tmp.append(hq.heappop(answer))
        return [tmp[-1], tmp[0]]