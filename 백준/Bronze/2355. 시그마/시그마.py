import sys
import math
input = sys.stdin.readline
a, b = map(int, input().split())
tmp = 0

if a > b:
    tmp = a
    a = b
    b = tmp

addition = a + b
multiple = math.ceil((b - a) / 2) 
if addition % 2 == 0: # 합이 짝수라면
    print(int(addition * multiple + (addition / 2)))
else: # 합이 홀수라면
    print(addition * multiple)
# elif a <= 0 and b <= 0:
    
#     addition = a + b
#     multiple = math.ceil((b + a) / 2) or -1
#     total = addition * multiple
#     # print(f'addition = {addition} multiple = {multiple}, total = {total}')
#     if addition % 2 == 0: # 합이 짝수라면
#         print(-(int(total - (addition / 2))))
#     else:
#         print(-total)
#         # print(-total) if total > 0 else print(total)
# elif a >= 0 and b <= 0:
#     positive_addition = a + 1 if a > 1 else a
#     positive_multiple = math.ceil((a - 1) / 2) or 1
#     negative_addition = b - 1 if b < -1 else b
#     negative_multiple = math.ceil((b + 1) / 2) or -1
#     positive_total = 0
#     negative_total = 0
    
#     if positive_addition % 2 == 0: # 양수 합이 짝수라면
#         positive_total = (positive_addition * positive_multiple) + (positive_addition / 2)
#     else:
#         positive_total = positive_addition * positive_multiple
        
#     if negative_addition % 2 == 0: # 음수 합이 짝수라면
#         negative_total = -((negative_addition * negative_multiple) - (negative_addition / 2))
#     else:
#         negative_total = -(negative_addition * negative_multiple)
        
#     print(int(positive_total + negative_total))
# elif a <= 0 and b >= 0:
#     positive_addition = b + 1 if b > 1 else b
#     positive_multiple = math.ceil((b - 1) / 2) or 1
#     negative_addition = a - 1 if a < -1 else a
#     negative_multiple = math.ceil((a + 1) / 2) or -1
#     positive_total = 0
#     negative_total = 0
    
#     if positive_addition % 2 == 0: # 양수 합이 짝수라면
#         positive_total = (positive_addition * positive_multiple) + (positive_addition / 2)
#     else:
#         positive_total = positive_addition * positive_multiple
        
#     if negative_addition % 2 == 0: # 음수 합이 짝수라면
#         negative_total = -((negative_addition * negative_multiple) - (negative_addition / 2))
#     else:
#         negative_total = -(negative_addition * negative_multiple)
        
#     print(int(positive_total + negative_total))
