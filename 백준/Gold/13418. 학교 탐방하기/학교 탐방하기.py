def solution(n, edges):
    best_case, worst_case = n, 0
    min_parent, max_parent = [i for i in range(n+1)], [i for i in range(n+1)]
    
    def get_parent(parent, x):
        if parent[x] == x:
            return x
        return get_parent(parent, parent[x])

    def find_parent(parent, a, b):
        a = get_parent(parent, a)
        b = get_parent(parent, b)
        
        if a == b:
            return True
        return False
            
    def union_parent(parent, a, b):
        a = get_parent(parent, a)
        b = get_parent(parent, b)
        
        if a < b:
            parent[b] = a
        else:
            parent[a] = b
    
    for a, b, downhill in edges:
        
        if downhill == 1:
            if not find_parent(min_parent, a, b):
                union_parent(min_parent, a, b)
                best_case -= 1
        else:
            if not find_parent(max_parent, a, b):
                union_parent(max_parent, a, b)
                worst_case += 1
        
    return worst_case**2 - best_case**2
    
n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m+1)]
result = solution(n, edges)
print(result)