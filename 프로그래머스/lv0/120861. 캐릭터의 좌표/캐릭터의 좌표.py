def checkValidation(limitBoard, current):
    h = limitBoard[0] // 2
    v = limitBoard[1] // 2    
    return current[0] >= -h and current[0] <= h and current[1] >= -v and current[1] <= v

def solution(keyinput, board):
    obj = {
        "left": [-1, 0],
        "right": [1, 0],
        "down": [0, -1],
        "up": [0, 1],
    }

    answer = [0, 0]
    
    for input in keyinput:
        moveAxisOfH = answer[0] + obj[input][0]
        moveAxisOfV = answer[1] + obj[input][1]
        if checkValidation(board, [moveAxisOfH, moveAxisOfV]):
            answer = [moveAxisOfH, moveAxisOfV]
            
    return answer