from collections import defaultdict
import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
words_dict = defaultdict(int)

for _ in range(N):
    word = input().rstrip()
    
    if len(word) >= M:
        words_dict[word] += 1
        
words_arr = sorted([[k, v] for k, v in words_dict.items()], key=lambda x: (-x[1], -len(x[0]), x[0]))
result = [x[0] for x in words_arr]

for r in result:
    print(r)