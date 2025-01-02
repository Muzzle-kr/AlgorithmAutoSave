def solution(k, dg):
    answer = 0
    n = len(dg)
    ch = [0] * n
    
    def dfs(current_k, count):
        nonlocal answer
        answer = max(answer, count)
        
        for j in range(n):
            if not ch[j] and current_k >= dg[j][0]:
                ch[j] = 1
                dfs(current_k - dg[j][1], count + 1)    
                ch[j] = 0        

    dfs(k, 0)
    return answer