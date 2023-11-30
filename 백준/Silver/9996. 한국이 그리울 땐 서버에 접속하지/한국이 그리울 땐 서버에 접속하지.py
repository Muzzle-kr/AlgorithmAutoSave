n = int(input())
pattern = input()
import re

for i in range(n):
    result = re.findall('^'+pattern.replace("*", ".*")+'$', input())
    if len(result) > 0:
        print("DA")
    else:
        print("NE")