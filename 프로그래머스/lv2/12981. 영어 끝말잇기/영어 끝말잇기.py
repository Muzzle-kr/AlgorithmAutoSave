def solution(n, words):
    
    lastSyllable = ""
    wordList = []
    for idx, i in enumerate(words):
        if idx == 0:
            wordList.append(i)
            lastSyllable = i[-1]
            continue
        
        if i[0] != lastSyllable:
            return [idx % n + 1, (idx)//n + 1]
            break
        elif i in wordList:
            return [idx % n + 1, (idx)//n + 1]
            break
        else:
            wordList.append(i)
            lastSyllable = i[-1]
            continue
    return [0, 0]