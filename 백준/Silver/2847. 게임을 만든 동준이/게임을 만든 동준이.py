import sys
input = sys.stdin.readline


N = int(input())
scores = []

for i in range(N):
    scores.append(int(input()))

decrease = 0

for i in range(N-2, -1, -1):
    if scores[i] >= scores[i+1]:
        decrease += (scores[i] - (scores[i+1] - 1))
        scores[i] = scores[i+1] - 1

print(decrease)