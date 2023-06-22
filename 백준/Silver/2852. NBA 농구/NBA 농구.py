n = int(input())

team_win_time = ["00:00", "00:00"]
team_score = [0, 0]
last_goal_time = "00:00"
last_goal_team = 0
def cal_diff_time(time1, time2):
    time2_min, time2_sec = map(int, time2.split(':'))
    time1_min, time1_sec = map(int, time1.split(':'))
    
    diff_min = time2_min - time1_min
    diff_sec = time2_sec - time1_sec
    if diff_sec < 0:
        diff_min -= 1
        diff_sec += 60
    
    return str(diff_min).zfill(2)+":"+str(diff_sec).zfill(2)

def add_time(time1, time2):
    time1_min, time1_sec = map(int, time1.split(':'))
    time2_min, time2_sec = map(int, time2.split(':'))
    
    add_min = time1_min + time2_min
    add_sec = time1_sec + time2_sec
    
    if add_sec > 59:
        add_min += 1
        add_sec -= 60
        
    return str(add_min).zfill(2)+":"+str(add_sec).zfill(2)

for _ in range(n):
    team_number, time = input().split()
    team_number = int(team_number)

    # 누군가 이기고 있던 상황이라면    
    if last_goal_team != 0:
        diff_time = cal_diff_time(last_goal_time, time)
        if team_score[0] > team_score[1]:
            team_win_time[0] = add_time(team_win_time[0], diff_time)
        elif team_score[0] < team_score[1]:
            team_win_time[1] = add_time(team_win_time[1], diff_time)
            
    last_goal_time = time
    last_goal_team = team_number
    team_score[team_number-1] += 1
    
# 마지막 48분까지 차이까지 더해주기
diff_time = cal_diff_time(last_goal_time, "48:00")
if team_score[0] > team_score[1]:
    team_win_time[0] = add_time(team_win_time[0], diff_time)
elif team_score[0] < team_score[1]:
    team_win_time[1] = add_time(team_win_time[1], diff_time)

for win_time in team_win_time:
    print(win_time)