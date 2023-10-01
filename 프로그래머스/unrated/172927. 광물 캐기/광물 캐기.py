import heapq as hq
    
def solution(picks, minerals):
    
    total_pick_cnt = sum(picks)
    
    limit_mienrals = minerals[0:total_pick_cnt*5]
    priority_queue = []
    
    answer = 0
    picks_dict = {
        "diamond": 0,
        "iron": 1,
        "stone": 2
    }
    
    pirodo_table_arr = [
        [1, 1, 1],
        [5, 1, 1],
        [25, 5, 1]
    ]
    
    cnt = 0
    pick_cnt_arr = [0, 0, 0]
    
    for idx, mineral in enumerate(limit_mienrals):
        # 광물 1개 저장하기
        pick_cnt_arr[picks_dict[mineral]] -= 1
        
        # 광물 캔 횟수 1개 추가
        cnt += 1
        
        # 광물을 5개가 찼을 때 작업
        if cnt == 5 or idx == len(minerals) -1:
            # 우선순위 큐 저장
            hq.heappush(priority_queue, pick_cnt_arr)
            
            # 캔 광물 갯수 초기화
            cnt = 0
            
            # 광물별 갯수 초기화
            pick_cnt_arr = [0, 0, 0]
            
    
    while priority_queue:
        diamond, iron, stone = hq.heappop(priority_queue)
        

        diamond = -diamond
        iron = -iron
        stone = -stone
        if picks[0] > 0:
            answer += pirodo_table_arr[0][0] * diamond + pirodo_table_arr[0][1] * iron + pirodo_table_arr[0][2] * stone
            picks[0] -= 1
            
        elif picks[1] > 0:
            answer += pirodo_table_arr[1][0] * diamond + pirodo_table_arr[1][1] * iron + pirodo_table_arr[1][2] * stone
            picks[1] -= 1
            
        elif picks[2] > 0:
            answer += pirodo_table_arr[2][0] * diamond + pirodo_table_arr[2][1] * iron + pirodo_table_arr[2][2] * stone
            picks[2] -= 1
            
        else:
            break    
    
    return answer


