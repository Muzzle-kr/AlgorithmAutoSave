def solution(n, computers):
    answer = 0
    visit = [0] * n
    
    def dfs(j):
        for idx, network in enumerate(computers[j]):
            # print(f'j: {j}, idx: {idx}, network: {network}, visit[idx]: {visit[idx]}')
            if network == 1 and visit[idx] == 0:
                visit[idx] = 1
                dfs(idx)
                
        return
    for i in range(n):
        isFind = False
        
        for j in range(n):
            if i != j:
                # 연결되었다면
                # print(f'i: {i}, j: {j} computers: {computers[i][j]}')
                if computers[i][j] == 1:
                    isFind = True
                    if visit[j] == 0:
                        # print(f'{i}와 {j}가 연결되었습니다.')
                        # 연결횟수 추가
                        answer += 1
                        visit[i] = 1
                        visit[j] = 1
                        dfs(j)
        if not isFind:
            # print(f'{i}는 네트워크 스스로 연결합니다')
            answer += 1
    return answer