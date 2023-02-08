import sys

input = sys.stdin.readline

N = int(input())

# 체스의 세로축(Index)에 대한 가로 좌표(Values)
row = [0] * N
answer = 0


def canPutChess(y):
    for i in range(y):
        if row[y] == row[i] or abs(row[y] - row[i]) == abs(y - i):
            return False
    return True


def putChess(y):
    if y == N:
        global answer
        answer += 1
        return

    for x in range(N):
        row[y] = x
        if canPutChess(y):
            putChess(y + 1)

putChess(0)
print(answer)