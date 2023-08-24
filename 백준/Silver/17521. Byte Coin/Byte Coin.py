N, W = map(int, input().split())
costs = [int(input()) for i in range(N)]

for i in range(N-1):
    if costs[i] < costs[i+1]:
        W = W // costs[i] * costs[i+1] + W % costs[i]

print(W)