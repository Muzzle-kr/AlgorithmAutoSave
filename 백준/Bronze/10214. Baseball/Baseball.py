N = int(input())

for _ in range(N):
    scoreOfY = 0
    scoreOfK = 0
    for i in range(9):
        Y, K = map(int, input().split())
        scoreOfY += Y
        scoreOfK += K
    if scoreOfY > scoreOfK:
        print("Yonsei")
    elif scoreOfK > scoreOfY:
        print("Korea")
    else: 
        print("Draw")