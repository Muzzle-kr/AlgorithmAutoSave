N, M = map(int, input().split())

if N == 0:
    print(0)
    exit()
    
books_weight = list(map(int, input().split()))

cnt = 0
total = 0

for idx, weight in enumerate(books_weight):
    
    # 박스를 하나 생성한다.
    if total == 0:
        cnt += 1
        
    if total + weight < M:
        total += weight
            
    elif total + weight == M:
        total = 0
        
    else:
        total = weight
        cnt += 1

print(cnt)
    
