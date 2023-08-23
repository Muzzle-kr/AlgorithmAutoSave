N, M = map(int, input().split())
piece = []
package = []

for _ in range(M):
    a, b = map(int, input().split())
    package.append(a)
    piece.append(b)

piece.sort()
package.sort()
ans = 0
while N > 6:
    if piece[0] * 6 < package[0]:
        ans += piece[0] * 6
    else:
        ans += package[0]
        
    N -= 6

if piece[0] * N < package[0]:
    ans += piece[0] * N
else:
    ans += package[0]

print(ans)
    
    
    