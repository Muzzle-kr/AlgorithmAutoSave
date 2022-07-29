import math
Y = (30, 10)
M = (60, 15)

N = int(input())
listCall = list(map(int, input().split()))
yCharge = 0
mCharge = 0

for i in listCall:
    yCharge += int(i // Y[0] * Y[1] + Y[1])
    mCharge += int(i // M[0] * M[1] + M[1])

if yCharge == mCharge:
    print(f"Y M {yCharge}")
elif yCharge > mCharge:
    print(f"M {mCharge}")
else:
    print(f"Y {yCharge}")


# 60으로 나눠서 나머지가 0이면 1배수
# 1이상이면 2배수