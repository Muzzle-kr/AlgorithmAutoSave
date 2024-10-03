N = int(input())
n_p, n_f, n_c, n_v = map(int, input().split())
ingres = [list(map(int, input().split())) for _ in range(N)]
min_price = float('inf')
answer= []

def recur(idx, p, f, c, v, price, ingres_list):
    global answer
    global min_price
    
    if idx == N:
        if p >= n_p and f >= n_f and c >= n_c and v >= n_v:
            if price < min_price:
                answer = [ingres_list]
                min_price = price
            elif price == min_price:
                answer.append(ingres_list)
        return
    
    recur(idx+1, p + ingres[idx][0], f + ingres[idx][1], c + ingres[idx][2], v + ingres[idx][3], price + ingres[idx][4], ingres_list + [idx+1])
    recur(idx+1, p, f, c, v, price, ingres_list)

recur(0, 0, 0, 0, 0, 0, [])

answer.sort()

if answer:
    print(min_price)
    print(*answer[0])
else:
    print(-1)