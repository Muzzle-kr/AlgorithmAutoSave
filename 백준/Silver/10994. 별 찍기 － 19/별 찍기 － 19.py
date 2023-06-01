def draw(n, idx):
    if n == 1:
        stars[idx][idx] = "*"
        return
    
    lens = 4 * n - 3
    
    for i in range(idx, lens+idx):
        # 위 아래
        stars[idx][i] = "*"
        stars[idx+lens-1][i] = "*"
        
        # 양 옆
        stars[i][idx] = "*"
        stars[i][idx+lens-1] = "*"

    return draw(n-1, idx+2)
        
n = int(input())
length = 4 * n - 3
stars = [[' '] * length for _ in range(length)]
draw(n, 0)

for i in range(length):
    for j in range(length):
        print(stars[i][j], end="")
    print()