def solution(id_list, report, k):
    length = len(id_list)
    idWithIdx = {key : idx for idx, key in enumerate(id_list)}
    reportList = [[] for i in range(length)]
    reported = [0 for i in range(length)]
    mail = [0 for i in range(length)]
    

    def findIdxWithName(n):
        for idx, name in enumerate(idWithIdx):
            if name == n:
                return idx
    
    def findNameWithIdx(idx):
        return list(idWithIdx.items())[idx][0]
    
    for i in report:
        a, b = i.split(" ")
        
        if b not in reportList[findIdxWithName(a)]:
            reportList[idWithIdx[a]].append(b)
            reported[idWithIdx[b]] += 1
    
    for i in range(length):
        name = findNameWithIdx(i)
        if reported[i] >= k:
            for j in range(length):
                if name in reportList[j]:
                    mail[j] += 1
                # 이름을 어떻게 할 것이냐..!
    return mail