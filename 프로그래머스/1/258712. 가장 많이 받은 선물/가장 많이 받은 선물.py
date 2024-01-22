from collections import defaultdict

def solution(friends, gifts):
    index_of_gifts = defaultdict(int)
    gift_give_get_dict = defaultdict(lambda:defaultdict(int))
    
    for gift in gifts:
        a, b = gift.split()
        
        # 보낸 선물이면 선물지수 +1
        index_of_gifts[a] += 1
        # 받은 선물이면 선물지수 -1
        index_of_gifts[b] -= 1
        
        gift_give_get_dict[a][b] += 1
    
    gifts_by_index = defaultdict(int)
    
    for a_f in friends:
        for b_f in friends:
            if a_f == b_f:
                continue
            
            # 주고 받은 기록이 있다면
            if gift_give_get_dict[a_f][b_f] != 0 or gift_give_get_dict[b_f][a_f] != 0:
                # 주고 받은 기록이 더 많은 경우 선물지수 +1
                if gift_give_get_dict[a_f][b_f] > gift_give_get_dict[b_f][a_f]:
                    gifts_by_index[a_f] += 1
                    continue
                elif gift_give_get_dict[a_f][b_f] == gift_give_get_dict[b_f][a_f]:
                    if index_of_gifts[a_f] > index_of_gifts[b_f]:
                        gifts_by_index[a_f] += 1
                        continue
            else:
                # 주고받은 기록이 없거나 주고 받은 기록이 같은 경우
                if index_of_gifts[a_f] > index_of_gifts[b_f]:
                    gifts_by_index[a_f] += 1
            # elif index_of_gifts[a_f] < index_of_gifts[b_f]:
            #     gifts_by_index[b_f] += 1
    
    answer = 0
    
    if gifts_by_index:
        answer = max(gifts_by_index.values())
    
    return answer