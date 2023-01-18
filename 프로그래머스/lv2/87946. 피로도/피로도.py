def solution(pirodo, dungeons):
    answer = []
    n = len(dungeons)
    ch = [0 for _ in range(n)]
    count = 0
    
    def DFS(pirodo, L, count):
        if L >= n:
            answer.append(count)
            return count
        else:
            for i in range(n):
                if ch[i] == 0:
                    ch[i] = 1
                    isPiro = False
                    if pirodo - dungeons[i][0] >= 0:
                        # print(f'현재 pirodo: {pirodo}, {L}번째 던전, 필요한 피로도: {dungeons[i][0]}, 깎이는 피로도: {dungeons[i][1]}, 이거 돌면 {count+1}개')
                        pirodo -= dungeons[i][1]
                        count += 1
                        isPiro = True
                    DFS(pirodo, L+1, count)
                    ch[i] = 0
                    if isPiro:
                        pirodo += dungeons[i][1]
                    count -= 1
    DFS(pirodo, 0, count)
    
    return max(answer)