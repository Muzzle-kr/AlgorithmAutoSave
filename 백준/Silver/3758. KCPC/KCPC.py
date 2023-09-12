from collections import defaultdict

for _ in range(int(input())):
    n, k, t, m = map(int, input().split())
    
    team_score_board = defaultdict(int)
    team_submit_cnt_board = defaultdict(int)
    team_answer_board = [[[0, 0] for _ in range(k+1)] for _ in range(n+1)]
    team_last_submit_time = defaultdict(int)
    
    for time in range(m):
        i, j, s = map(int, input().split())
        
        # 한 번도 제출 안했을 때
        if team_answer_board[i][j][0] == 0:
            team_answer_board[i][j] = [s, time]
            team_score_board[i] += s
        # 제출을 한 번 했던 경우
        else:
            # 점수가 더 높을 때 처리
            if s > team_answer_board[i][j][0]:
                team_score_board[i] += s - team_answer_board[i][j][0]
                team_answer_board[i][j] = [s, time]
                
        team_submit_cnt_board[i] += 1
        team_last_submit_time[i] = time
        
    result = [(i, team_score_board[i], team_submit_cnt_board[i], team_last_submit_time[i]) for i in range(1, n+1)]
    result.sort(key=lambda x: (-x[1], x[2], x[3]))
    
    for i in range(len(result)):
        if result[i][0] == t:
            print(i+1)
            break
        