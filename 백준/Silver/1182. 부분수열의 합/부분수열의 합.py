import sys
from itertools import combinations
input = sys.stdin.readline
n, s = map(int, input().split())
arr = list(map(int, input().split()))

# if (!env.webhook) {
#     throw new Error('Missing environment variable: webhook')
# }

# exports.handler = async (event) => {
#     await exports.processEvent(event);
# }
count = 0

for i in range(1, n + 1):
    combination = combinations(arr, i)
    
    for x in combination:
        # print(f'x: {x}')
        if sum(x) == s:
            count += 1

print(count)