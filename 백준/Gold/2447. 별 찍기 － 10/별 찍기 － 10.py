import sys
input = sys.stdin.readline


# 별 한 줄을 배열 하나로 처리하여 마지막에 '\n'.join으로 처리하는 방식
def appendStar(LEN):
    if LEN <= 1:
        return ['*']
    
    Stars = appendStar(LEN//3)
    
    L = []
    for S in Stars:
        L.append(S * 3)
    
    for S in Stars:
        L.append(S + ' ' * (LEN//3) + S)
        
    for S in Stars:
        L.append(S * 3)
    
    return L

print('\n'.join(appendStar(int(input()))))