import sys
input = sys.stdin.readline
from copy import deepcopy

result = []
w = 0
b = 0
modeArr = ['W', 'B']
M, N = map(int, input().split())
chessBoard = []


for _ in range(M):
    chessBoard.append(list(input().rstrip()))
    
row = 0
col = 0

# print(f'chessBoard : {chessBoard}, rowLength: {len(chessBoard)}, colLength: {len(chessBoard[0])}')

while row + 8 <= len(chessBoard):
    while col + 8 <= len(chessBoard[0]):
        for mode in modeArr:
            if mode == 'W':
                chessBoardWithWhite = deepcopy(chessBoard)
                lastColor = 'B'
                # 첫 인덱스(줄)
                for i in range(row, row + 8):
                    for j in range(col, col + 8):
                        # print(f'mode: {mode}, row: {row} col: {col}, i: {i}, j: {j}')
                        if i == row:
                            # 마지막 컬러랑 같으면 
                            if chessBoardWithWhite[i][j] == lastColor:
                                # print('chessBoardWithWhite[i][j]와 마지막 컬러가 같습니다.')
                                if lastColor == "B":
                                    chessBoardWithWhite[i][j] = "W"
                                else:
                                    chessBoardWithWhite[i][j] = "B"
                                w += 1
                        else:
                            if chessBoardWithWhite[i][j] == chessBoardWithWhite[i-1][j]:
                                # print('chessBoardWithWhilte[i][j]와 [i-1][j] 컬러가 같습니다.')
                                if chessBoardWithWhite[i-1][j] == "B":
                                    chessBoardWithWhite[i][j] = "W"
                                else:
                                    chessBoardWithWhite[i][j] = "B"
                                w += 1
                        lastColor = chessBoardWithWhite[i][j]   
            else: 
                chessBoardWithBlack = deepcopy(chessBoard)
                lastColor = 'W'
                for i in range(row, row + 8):
                    for j in range(col, col + 8):
                        # 첫 인덱스(줄)
                        if i == row:
                            # 마지막 컬러랑 같으면 
                            if chessBoardWithBlack[i][j] == lastColor:
                                # print('chessBoardWithBlack[i][j]와 마지막 컬러가 같습니다.')
                                if lastColor == "B":
                                    chessBoardWithBlack[i][j] = "W"
                                else:
                                    chessBoardWithBlack[i][j] = "B"
                                b += 1
                        else:
                            if chessBoardWithBlack[i][j] == chessBoardWithBlack[i-1][j]:
                                # print('chessBoardWithBlack[i][j]와 [i-1][j] 컬러가 같습니다.')
                                if chessBoardWithBlack[i-1][j] == "B":
                                    chessBoardWithBlack[i][j] = "W"
                                else:
                                    chessBoardWithBlack[i][j] = "B"
                                b += 1
                        lastColor = chessBoardWithBlack[i][j]      
        # print(f'w: {w}, b: {b}')
        result.append(min(w, b))
        w = 0
        b = 0
            
        col += 1
    col = 0
    row += 1
# print(f'result: {result}')
print(min(result))
        # M * N만큼 돌아야하고, 2번 돌아야함 