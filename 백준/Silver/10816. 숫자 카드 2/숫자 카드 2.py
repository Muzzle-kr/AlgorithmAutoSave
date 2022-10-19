from bisect import bisect_left, bisect_right
from sys import stdin

N = stdin.readline().rstrip()
card = list(map(int,stdin.readline().split()))
M = stdin.readline().rstrip()
targetCard = list(map(int,stdin.readline().split()))
card.sort()

def count_by_range(a, targetValue):
    right_index = bisect_right(a, targetValue)
    left_index = bisect_left(a, targetValue)
    return right_index - left_index


for i in range(len(targetCard)):
    print(count_by_range(card, targetCard[i]), end=' ')