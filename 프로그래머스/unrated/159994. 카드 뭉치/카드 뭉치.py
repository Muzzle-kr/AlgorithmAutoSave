def solution(cards1, cards2, goal):
    answer = ''
    cards1Index = 0
    cards2Index = 0
    
    while goal:
        # print(f'goal: {goal}, cards1Index: {cards1Index}, cards2Index: {cards2Index}')
        isFind = False
        
        if cards1Index < len(cards1) and goal[0] == cards1[cards1Index]:
            cards1Index += 1
            isFind = True
        elif cards2Index < len(cards2) and goal[0] == cards2[cards2Index]:
            cards2Index += 1
            isFind = True
        
        if isFind:
            goal = goal[1:]
        else:
            return "No"
    
    return "Yes"