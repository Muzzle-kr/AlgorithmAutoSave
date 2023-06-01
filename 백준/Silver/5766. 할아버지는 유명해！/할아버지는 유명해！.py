while True:
    rank = [0 for _ in range(10001)]
    n, m = map(int, input().split())

    if n == 0 and m == 0:
        break

    for _ in range(n):
        weekly_rank = map(int, input().split())
        
        for r in weekly_rank:
            rank[r] += 1
            
    new_rank = {}

    for idx, r in enumerate(rank):
        if r != 0:
            new_rank[idx] = r
            
    final_rank = sorted(new_rank.items(), key=lambda x: x[1], reverse=True)
    
    winner_score = final_rank[0][1]
    second_score = 0
    ans = []
    for n, score in final_rank:
        if score == winner_score:
            continue

        # print(f'n: {n} score: {score}, second_score: {second_score}, winner_score: {winner_score}')
        if second_score == 0 and score != winner_score:
            second_score = score
            ans.append(n)
        else:
            if second_score == score:
                ans.append(n)
            else:
                break
    print(*sorted(ans))