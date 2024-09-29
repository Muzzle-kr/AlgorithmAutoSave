def solution():
    bingo = [list(map(int, input().split())) for i in range(5)]
    bingo_map = [[False for i in range(5)] for _ in range(5)]
    numbers = []
    answer = 0
    
    for _ in range(5):
        numbers += list(map(int, input().split()))

    for idx, number in enumerate(numbers):
        drawBingo(number, bingo, bingo_map)
        isBingo = checkBingo(bingo_map)
        if isBingo:
            answer = idx + 1
            break
        
    return answer


def drawBingo(number, bingo, bingo_map):
    for i in range(5):
        for j in range(5):
            if bingo[i][j] == number:
                bingo_map[i][j] = True
                is_breakable = True
                return

            
def checkBingo(bingo_map):
    answer = 0
    
    # 세로 체크
    for i in range(5):
        if all(bingo_map[j][i] for j in range(5)):
            answer += 1
            
    # 가로
    for j in range(5):
        if all(bingo_map[j][i] for i in range(5)):
            answer += 1
    
    # 대각선1
    if all(bingo_map[i][i] for i in range(5)):
        answer += 1
        
    # 대각선2
    if all(bingo_map[4-i][i] for i in range(5)):
        answer += 1
    
    return answer >= 3

print(solution())