N = int(input())
ingres = [list(map(int, input().split())) for _ in range(N)]
answer = float('inf')

def recur(idx, sour, bitter, use):
    global answer
    if idx == N:
        if use > 0:
            answer = min(answer, abs(sour - bitter))
        return
    
    # 사용
    recur(idx+1, sour * ingres[idx][0], bitter + ingres[idx][1], use + 1)
    
    # 미사용
    recur(idx+1, sour, bitter, use)

recur(0, 1, 0, 0)
print(answer)