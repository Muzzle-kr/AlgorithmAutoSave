def getParent(parent, x):
    if parent[x] == x:
        return x
    return getParent(parent, parent[x])
        
def solution(n, costs):
    answer = 0
    costs = sorted(costs, key=lambda x: x[2])
    cycle = [i for i in range(n + 1)]
    
    
    def unionParent(parent, a, b):
        a = getParent(parent, a)
        b = getParent(parent, b)
        if a < b:
            parent[b] = a
        else:
            parent[a] = b
        
    def findParent(parent, a, b):
        a = getParent(parent, a)
        b = getParent(parent, b)
        if a == b:
            return True
        else:
            return False
        
    for c in costs:
        start, end, cost = c
        
        # 한쪽이 완전 비어야한다 // Non-Cycle
        
        if not findParent(cycle, start, end):
            answer += cost
            unionParent(cycle, start, end)    
        
        
    return answer