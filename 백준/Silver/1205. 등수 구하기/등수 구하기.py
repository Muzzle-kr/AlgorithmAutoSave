N, taesoo_score, P = map(int, input().split())

if N == 0:
    print(1)
    exit()

    
scores = list(map(int, input().split()))
scores.sort(reverse=True)        
scores = scores[:P+1]
grade = 0

if N < P:
    for _ in range(P-N):
        scores.append(-1)

        
for i in range(P-1, -1, -1):
    if scores[i] < taesoo_score:
        grade = i + 1
        continue
    elif scores[i] == taesoo_score:
        if N == P and i == N-1:
            grade = -1
            break
        grade = i + 1
    else:
        break

if grade <= 0:
    print(-1)
else:
    print(grade)