from collections import defaultdict

def solution(genres, plays):
    answer = []
    genres_dict = defaultdict(int)
    
    
    
    for i in range(len(genres)):
        genres_dict[genres[i]] += plays[i]
    
    total_list = [[genres_dict[genres[i]], genres[i], plays[i], i] for i in range(len(genres))]
    total_list.sort(key=lambda x: (-x[0], -x[2], x[3]))
    
    contain_cnt_dict = defaultdict(int)
    result = []
    
    for i in range(len(total_list)):
        if contain_cnt_dict[total_list[i][1]] < 2:
            contain_cnt_dict[total_list[i][1]] += 1
            result.append(total_list[i][3])
    
    return result