import sys
input = sys.stdin.readline

num = int(input())
sortedNum = sorted(str(num), reverse=True)
print(int(''.join(sortedNum)))