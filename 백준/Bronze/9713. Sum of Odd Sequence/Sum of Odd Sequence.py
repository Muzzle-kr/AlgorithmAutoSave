N = int(input())

# 1부터 주어진 수까지의 모든 홀수의 합을 출력하라
for i in range(N):
    num = int(input())
    sum = 0
    for j in range(1, num + 1, 2):
        sum += j
    
    print(sum)