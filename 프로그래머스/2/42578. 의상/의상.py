from collections import defaultdict
def solution(clothes):
    answer = 0
    clothes_dict = defaultdict(list)
    
    for cloth, group in clothes:
        clothes_dict[group].append(cloth)
    
    
    if len(clothes_dict) > 1:
        total = 1
        
        for key, val in clothes_dict.items():
            total *= len(val) + 1
        
        return total - 1
        
    else:
        for key, val in clothes_dict.items():
            return len(val)
    

