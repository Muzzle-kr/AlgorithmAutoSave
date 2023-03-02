n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]
answer = [0, 0, 0]

def divide(x, y, n):
    mark = paper[x][y]
    
    for i in range(x, x + n):
        for j in range(y, y + n):
            next = n // 3
            
            if paper[i][j] != mark:
                for k in range(3):
                    for l in range(3):
                        divide(x + next * k, y + next * l, next)
                return
        
    answer[mark+1] += 1
    return 
divide(0, 0, n)

for a in answer:
    print(a)