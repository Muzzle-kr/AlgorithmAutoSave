N = int(input())

count = [[1, 0], [0, 1]]
for i in range(2, 41):
    count.append([count[i-2][0] + count[i-1][0], count[i-2][1] + count[i-1][1]])
    

for i in range(N):
    num = int(input())
    print(*count[num])