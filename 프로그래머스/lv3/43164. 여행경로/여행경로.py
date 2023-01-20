def solution(tickets):
    
    
    def dfs(arr):
        # print(f'arr: {arr} ')
        if len(arr) == length + 1:
            answer.append(arr)
            return
        
        for i in range(len(tickets)):
            # check가 안되어있는 곳 중
            if not check[i] and arr[-1] == tickets[i][0]:
                check[i] = True
                dfs(arr + [tickets[i][1]])
                check[i] = False
                
        
    answer = []
    tickets = sorted(tickets, key=lambda x: (x[0], x[1]))
    length = len(tickets)
    check = [False] * len(tickets)
    
    for i in range(len(tickets)):
        if tickets[i][0] == "ICN":
            check[i] = True
            dfs([tickets[i][0], tickets[i][1]])
            check[i] = False
    
    return sorted(answer)[0]