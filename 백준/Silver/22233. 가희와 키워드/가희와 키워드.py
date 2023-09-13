from collections import defaultdict
import sys
import copy

def writeKeyword(arr):
    global keyword
    for keyword in arr:
        keywords[keyword] -= 1
    
    return list(keyword.values()).count(1)

input = sys.stdin.readline
N, M = map(int, input().rstrip().split())
keyword_dict = {}
arr = []
keyword_set = set()

for i in range(N):
    keyword_set.add(input().rstrip())

for _ in range(M):
    keywordArr = list(input().rstrip().split(","))
    
    for keyword in keywordArr:
        try:
            keyword_set.remove(keyword)
        except:
            continue
    print(len(keyword_set))