def solution(dots):
    firstX = dots[0][0]
    firstY = dots[0][1]
    
    secondX = dots[1][0]
    secondY = dots[1][1]
    
    thirdX = dots[2][0]
    thirdY = dots[2][1]
    
    fourthX = dots[3][0]
    fourthY = dots[3][1]
    
    # 0, 1 번째랑 2, 3번째 비교
    diffX1 = firstX - secondX
    diffY1 = firstY - secondY
    diffX2 = thirdX - fourthX
    diffY2 = thirdY - fourthY
    # print(diffX1, diffY1, diffX2, diffY2)
    if diffX1 / diffY1 == diffX2 / diffY2:
        return 1
    
    # 0, 2번째 // 1, 3번째 비교    
    diffX1 = firstX - thirdX
    diffY1 = firstY - thirdY
    diffX2 = fourthX - secondX
    diffY2 = fourthY - secondY
    # print(diffX1, diffY1, diffX2, diffY2)
    if diffX1 / diffY1 == diffX2 / diffY2:
        return 1

    # 0, 3번째 // 1, 2번째 비교    
    diffX1 = firstX - fourthX
    diffY1 = firstY - fourthY
    diffX2 = thirdX - secondX
    diffY2 = thirdY - secondY
    
    # print(diffX1, diffY1, diffX2, diffY2)
    if diffX1 / diffY1 == diffX2 / diffY2:
        return 1
    
    return 0