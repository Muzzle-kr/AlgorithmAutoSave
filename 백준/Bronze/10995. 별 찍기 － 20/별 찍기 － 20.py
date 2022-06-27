# 홀수일 경우 "* "
# 짝수일 경우 " *"
repeat = int(input())

for i in range(1, repeat + 1):
    if i % 2 == 1: # 홀수라면
        print(("* " * repeat).rstrip())
    else: # 짝수라면
        print(" *" * repeat)