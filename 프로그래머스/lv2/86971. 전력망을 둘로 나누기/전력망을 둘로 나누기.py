def dfs(start):
    global obj
    global wireCount
    
    if obj[start] == 0:
        return
    
    for v in obj[start]:
        if checkWire[v] == 1:
            continue
        else: 
            checkWire[v] = 1
            wireCount += 1
            dfs(v)
            
            
            
def solution(n, wires):
    chk = [0] * (n + 1) 
    answer = 9999
    
    wires = sorted(wires, key=lambda x: (x[0], x[1]))
    
    for idx, wire in enumerate(wires):
        global obj
        global checkWire
        global wireCount
        checkWire = [0] * (n+1)
        treeCount = 0
        chk[idx] = 1
        wireCount = 0    
        wireCountArr = []

        obj = {}
        for i, w in enumerate(wires):
            a, b = w
            if chk[i] == 1:
                continue
            if chk[i] == 0:
                if a not in obj:
                    obj[a] = [b]
                else:
                    obj[a].append(b)
                    
                if b not in obj:
                    obj[b] = [a]
                else:
                    obj[b].append(a)
        
        
        for wireItem in list(obj.items()):
            start, _ = wireItem
            
            wireCount = 0
            
            if checkWire[start] == 0:
                checkWire[start] = 1
                dfs(start)
                wireCount += 1
                treeCount += 1
                # print(f'treeCount: {treeCount}, wireCountArr: {wireCountArr}, 자른 와이어: {wire}')
                answer = min(answer, abs(n - 2 * wireCount))
                # print(f'answer: {answer}')
                wireCountArr.append(wireCount) 

        
        # if treeCount == 2:
        #     # print(f'treeCount: {treeCount}, wireCountArr: {wireCountArr}, 자른 와이어: {wire}, 송전탑 갯수차이: {abs(wireCountArr[0] - wireCountArr[1])}')
        #     answer = min(answer, abs(wireCountArr[0] - wireCountArr[1]))
        # if treeCount == 1:
        #     # print(f'treeCount: {treeCount}, wireCountArr: {wireCountArr}, 자른 와이어: {wire}, 송전탑 갯수차이: {abs(wireCountArr[0])}')
        #     answer = min(answer, abs(wireCountArr[0]))
        chk[idx] = 0
    return answer