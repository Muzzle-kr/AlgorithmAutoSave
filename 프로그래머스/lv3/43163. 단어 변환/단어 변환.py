def isDifferenceOne(a, b):
    diffCnt = 0

    for i in range(len(a)):
        if a[i] != b[i]:
            diffCnt += 1

    return diffCnt == 1


def dfs(words, target, word, count, route):
        global answer
        global chk
        if word == target:
            answer.append(count)
            return
        
        for i in range(len(words)):
            if isDifferenceOne(words[i], word) and chk[i] != 1:
                chk[i] = 1
                dfs(words, target, words[i], count + 1, route + [words[i]])
                chk[i] = 0
                
    
    
def solution(begin, target, words):
    global answer
    global chk
    answer = []
    chk = [0] * len(words)
    
    if target not in words:
        return 0
    
    for idx, w in enumerate(words):
        count = 0
        changeableWord = begin

        if isDifferenceOne(w, changeableWord) and chk[idx] != 1:    
            changeableWord = w
            chk[idx] = 1    
                    
            if changeableWord == target:
                return count + 1
            
            dfs(words, target, changeableWord, count + 1, [begin, w])
            chk[idx] = 0
            count -= 1

    if answer:
        return min(answer)
    else:
        return 0