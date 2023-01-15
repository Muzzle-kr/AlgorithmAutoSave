def solution(priorities, location):
    answer = 1
    maxValue = max(priorities)
    targetIndex = location
    # 지금 앞에 나온 게 최대값인 지 확인
    
    # targetIndex는 pop이 되면 length값이 되고, index가 -1씩 줄어들어 0이되면 뽑음
    
    while True:
        document = priorities.pop(0)
            
        # print(f'document: {document}, priorities: {priorities}, targetIndex: {targetIndex}, answer: {answer}')
        if document == maxValue:
            # print("출력 대상: {document}")
            if targetIndex == 0:
                # print("목표값을 찾았습니다.: {document}")
                break
            else:
                maxValue = max(priorities)
                answer += 1
                targetIndex -= 1
        elif document < maxValue:
            priorities.append(document)
            
            if targetIndex == 0:
                targetIndex = len(priorities) - 1
            else:
                targetIndex -= 1
                
        
    return answer