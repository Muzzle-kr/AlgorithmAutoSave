def solution(n, words):
    
    lastSyllable = ""
    wordList = []
    for idx, i in enumerate(words):
        # print(f'{idx+1}번째 사람이 말한 단어는 {i}이며 시작단어는 {lastSyllable}이어야합니다.')
        
        if idx == 0:
            wordList.append(i)
            lastSyllable = i[-1]
            continue
        
        if i[0] != lastSyllable:
            return [idx % n + 1, (idx)//n + 1]
            break
        elif i in wordList:
            # print(f'{i}는 이미 말한 단어입니다.')
            return [idx % n + 1, (idx)//n + 1]
            break
        else:
            wordList.append(i)
            lastSyllable = i[-1]
            continue
            
            
    # print(f'wordList : {wordList}')
    return [0, 0]