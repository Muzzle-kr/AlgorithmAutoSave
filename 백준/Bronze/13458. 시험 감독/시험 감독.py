import sys
import math
input = sys.stdin.readline
total = 0 # 총 감독관 수

N = int(input())
test_site = list(map(int, input().split()))
count_manage_commander, count_manage_manager = map(int, input().split())

for i in range(N):
    rest = test_site[i] - count_manage_commander
    total += 1 # 총 감독관 수 + 1
    if rest > 0:
        total += math.ceil(rest / count_manage_manager) or 1
        # rest -= count_manage_manager
        # count_manager += 1 # 부 감독관 수 + 1

print(total)