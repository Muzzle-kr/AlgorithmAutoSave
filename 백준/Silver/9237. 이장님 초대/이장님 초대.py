n = int(input())
trees = list(map(int, input().split()))
trees.sort(reverse=True)
answer = 0

for idx, tree in enumerate(trees):
    answer = max(answer, tree + idx + 2)

print(answer)