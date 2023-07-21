def get_dist(n, edges):  
    best_case, worst_case = n, 0
    max_parent, min_parent = [i for i in range(n+1)], [i for i in range(n+1)]
    
    def get_parent(x, parent):
        if parent[x] == x:
            return x
        return get_parent(parent[x], parent)

    def find_parent(a, b, parent):
        a = get_parent(a, parent)
        b = get_parent(b, parent)
        
        if a == b:
            return True
        return False

    def union_parents(a, b, parent):
        a = get_parent(a, parent)
        b = get_parent(b, parent)
        
        if a > b:
            parent[a] = b
        else:
            parent[b] = a
    
    
    for n1, n2, w in edges:
        
        # 내리막길일 때
        if w == 1:
            if not find_parent(n1, n2, min_parent): 
                union_parents(n1, n2, min_parent)
                best_case -= 1
        else:     
            if not find_parent(n1, n2, max_parent): 
                union_parents(n1, n2, max_parent)
                worst_case += 1
                
    return worst_case**2 - best_case**2 
        

n, m = map(int, input().split())        
edges = [tuple(map(int, input().split())) for _ in range(m+1)]
result = get_dist(n, edges)
print(result)