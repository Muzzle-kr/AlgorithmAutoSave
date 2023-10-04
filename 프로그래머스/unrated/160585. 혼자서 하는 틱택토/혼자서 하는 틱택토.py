def solution(board: list) -> int:
    board: list = [list(i) for i in board]
    visit: list = [[0] * 3 for _ in range(3)]
    
    # O, X 갯수
    o: int = 0
    x: int = 0
    
    # 0: 가로, 1: 세로, 2: 대각선
    o_condition = [False] * 3
    x_condition = [False] * 3
    
    def checkVictoryCondition(x: int, y: int, mark: str, board: list) -> None:
            # 가로축 확인
        checkHorizontal = True
        # 세로축 확인
        checkVertical = True
        # 방문 여부
        visit[x][y] = 1

        # 가로축 확인 반복문
        for i in range(1, 3):
            if 0 <= x + i <= 2 and visit[x + i][y] == 0:
                if board[x + i][y] != mark:
                    checkHorizontal = False
            if 0 <= x - i <= 2 and visit[x - i][y] == 0:
                if board[x - i][y] != mark:
                    checkHorizontal = False
            if not checkHorizontal:
                break  # 더 이상 확인할 필요 없음
        
        if checkHorizontal:
            if mark == "O":
                o_condition[0] = True
            else:
                x_condition[0] = True

        # 세로축 확인 반복문
        for i in range(1, 3):
            if 0 <= y + i <= 2 and visit[x][y + i] == 0:
                if board[x][y + i] != mark:
                    checkVertical = False
            if 0 <= y - i <= 2 and visit[x][y - i] == 0:
                if board[x][y - i] != mark:
                    checkVertical = False
            if not checkVertical:
                break  # 더 이상 확인할 필요 없음
        
        if checkVertical:
            if mark == "O":
                o_condition[1] = True
            else:
                x_condition[1] = True
                
        # 대각선 축 확인 반복문
        if (x == 0 or x == 2) and (y == 0 or y == 2):
            checkDiagonal = True
            check = [(0, 0), (2, 2), (0, 2), (2, 0)]
            direction = [(1, 1), (-1, -1), (1, -1), (-1, 1)]

            dx = x
            dy = y

            for _ in range(2):
                dx += direction[check.index((x, y))][0]
                dy += direction[check.index((x, y))][1]

                if 0 <= dx <= 2 and 0 <= dy <= 2 and visit[dx][dy] == 0:
                    if board[dx][dy] != mark:
                        checkDiagonal = False
                        break

            if checkDiagonal:
                if mark == "O":
                    o_condition[2] = True
                else:
                    x_condition[2] = True

        # 함수 종료 전에 visit 리스트 초기화
        visit[x][y] = 0

    
    for i in range(3):
        for j in range(3):
            if board[i][j] == "O":
                o += 1
                checkVictoryCondition(i, j, board[i][j], board)
            elif board[i][j] == "X":
                x += 1
                checkVictoryCondition(i, j, board[i][j], board)
    
    # 2개면 안됨
    oCount: int = o_condition.count(True)
    xCount: int = x_condition.count(True)
    
    # 갯수 차이로 인한 오류 판별
    if o - x > 1 or x > o or (o + x == 9 and o - x != 1):
        return 0
            
    # 1줄 만들기 오류 판별
    if (oCount > 0 and o <= x) or (xCount > 0 and o > x):
        return 0
        
    # "O" 승리 조건 판별
    if oCount == 3 and x >= o:
        return 0
    
    # "X" 승리 조건 판별
    if xCount == 3 and oCount > xCount:
        return 0

    return 1