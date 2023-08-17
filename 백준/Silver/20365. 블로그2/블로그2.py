import sys
from collections import defaultdict

input = sys.stdin.readline
N = int(input())
word = list(input().rstrip())
dic = defaultdict(int)
dic[word[0]] = 1

for i in range(1, N):
    if word[i] != word[i-1]:
        dic[word[i]] += 1

print(min(dic["R"], dic["B"])+1)