from collections import defaultdict

def solution(friends, gifts):
    gifts_given = defaultdict(int)
    gifts_received = defaultdict(int)
    gifts_between = defaultdict(lambda: defaultdict(int))
    
    for gift in gifts:
        giver, receiver = gift.split()
        gifts_given[giver] += 1
        gifts_received[receiver] += 1
        gifts_between[giver][receiver] += 1
    
    # 각 친구의 선물 지수 계산
    gift_index = {}
    
    for friend in friends:
        gift_index[friend] = gifts_given[friend] - gifts_received[friend]
    
    # 다음 달에 받을 선물 수를 저장할 딕셔너리
    next_month_gifts = defaultdict(int)
    
    for i in range(len(friends)):
        for j in range(i+1, len(friends)):
            friend1 = friends[i]
            friend2 = friends[j]

            # 친구 쌍의 선물 주고받은 횟수
            given1_to_2 = gifts_between[friend1][friend2]
            given2_to_1 = gifts_between[friend2][friend1]
            
            if given1_to_2 + given2_to_1 > 0:
                
                if given1_to_2 > given2_to_1:
                    next_month_gifts[friend1] += 1
                elif given1_to_2 < given2_to_1:
                    next_month_gifts[friend2] += 1
                else:
                    if gift_index[friend1] > gift_index[friend2]:
                        next_month_gifts[friend1] += 1
                    elif gift_index[friend1] < gift_index[friend2]:
                        next_month_gifts[friend2] += 1
            else:
                if gift_index[friend1] > gift_index[friend2]:
                    next_month_gifts[friend1] += 1
                elif gift_index[friend1] < gift_index[friend2]:
                    next_month_gifts[friend2] += 1
            
    if next_month_gifts:
        return max(next_month_gifts.values())
    else:
        return 0