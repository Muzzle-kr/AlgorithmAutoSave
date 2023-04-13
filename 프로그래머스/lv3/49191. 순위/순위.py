from collections import defaultdict

def solution(n, results):
    answer = 0
    winner_dict = defaultdict(set)
    loser_dict = defaultdict(set)
    
    for winner, loser in results:
        winner_dict[winner].add(loser)
        loser_dict[loser].add(winner)
        
    # 나를 이긴 사람은 내가 이긴 사람들보다도 강하다
    
    for i in range(1, n+1):
        for winner in winner_dict[i]:
            loser_dict[winner].update(loser_dict[i])
        
        for loser in loser_dict[i]:
            winner_dict[loser].update(winner_dict[i])
            
    for i in range(1, n+1):
        if len(winner_dict[i]) + len(loser_dict[i]) == n-1:
            answer += 1
    return answer