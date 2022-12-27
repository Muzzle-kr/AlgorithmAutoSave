import copy

def solution(board):
    answer = 0
    newBoard = copy.deepcopy(board)
    def checkValidation(x, y, limitX, limitY):
        return x >= 0 and x <= limitX and y >= 0 and y <= limitY
    
    def blowup(coordinate):
        lengthY = len(board)
        lengthX = len(board[0])
        scope = [[0, 1], [1, 1], [1, -1], [-1, 1], [-1, -1], [1, 0], [-1, 0], [0, -1]]

        
        for i in scope:
            moveX = coordinate[0] + i[0]
            moveY = coordinate[1] + i[1]
            if checkValidation(moveX, moveY, lengthX-1, lengthY-1):
                if newBoard[moveX][moveY] != 1:
                    newBoard[moveX][moveY] = 1
        return;   
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 1:
                blowup([i, j])

    for i in newBoard:
        for j in i:
            if j == 0:
                answer += 1

    return answer