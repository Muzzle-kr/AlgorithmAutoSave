def solution(players, callings):    
    
    dic = dict()
    
    for idx, player in enumerate(players):
        dic[player] = idx
    
    for call in callings:
        pre, post = dic[call]-1, dic[call]
        dic[players[pre]], dic[players[post]] = dic[players[post]], dic[players[pre]]
        players[pre], players[post] = players[post], players[pre]
        
    players = [item[0] for item in sorted(dic.items(), key=lambda x: x[1])]
    return players