from collections import defaultdict
import sys
input = sys.stdin.readline
dict = defaultdict(int)
total = 0
while True:
    word = input().rstrip()
    if not word:
        break
    total += 1
    
    dict[word] += 1
    
dict = sorted(dict.items(), key=lambda x: (x[0]))
for i in range(len(dict)):
    print(dict[i][0], '%.4f' % (dict[i][1]/total*100))