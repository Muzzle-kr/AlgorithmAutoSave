import heapq as hq

def solution(genres, plays):
    
    answer = []
    
    playCountObj = {}
    playCountRankObj = {}
    
    for i in range(len(plays)):
        if genres[i] in playCountObj:
            playCountObj[genres[i]] += plays[i]
            if plays[i] in playCountRankObj[genres[i]]:
                playCountRankObj[genres[i]][plays[i]].append(i)
            else:
                playCountRankObj[genres[i]][plays[i]] = [i]
        else:
            playCountObj[genres[i]] = plays[i]
            playCountRankObj[genres[i]] = {plays[i]: [i]}
    
    # print(f'장르 Obj: {playCountObj}')
    # print(f'랭크 Obj: {playCountRankObj}')
    
    for genre in sorted(playCountObj, key=lambda x: playCountObj[x], reverse=True):
        arr = sorted(playCountRankObj[genre].items(), key=lambda x: x[0], reverse=True)[:2]
        
        # print(f'선택된 장르: {genre}')
        # print(f'{genre} 랭크 현황: {arr}')
        
        for i in arr[:2]:
            # print(i[1], len(i[1]))
            if len(i[1]) == 2:
                answer.append(i[1][0])
                answer.append(i[1][1])
                break
            answer.append(*i[1])
        
    return answer