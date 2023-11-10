def solution(board, skill):
    answer = 0
    n = len(board)
    m = len(board[0])
    arr = [[0] * (m+1) for _ in range(n+1)]
        
    for type, r1, c1, r2, c2, degree in skill:
        if type == 1:
            degree *= -1
        
        arr[r1][c1] += degree
        arr[r1][c2+1] -= degree
        arr[r2+1][c1] -= degree
        arr[r2+1][c2+1] += degree
        
    # 가로 방향 누적합
    for i in range(n):
        for j in range(1, m):
            arr[i][j] += arr[i][j-1]
            
    
    for i in range(1, n):
        for j in range(m):
            arr[i][j] += arr[i-1][j]
    

    for i in range(len(board)):
        for j in range(len(board[0])):
            board[i][j] += arr[i][j]
            if board[i][j] > 0:
                answer += 1
    return answer