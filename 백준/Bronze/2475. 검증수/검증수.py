import math

n1, n2, n3, n4, n5 = map(int, input().split())

n1 = math.pow(n1, 2)
n2 = math.pow(n2, 2)
n3 = math.pow(n3, 2)
n4 = math.pow(n4, 2)
n5 = math.pow(n5, 2)


print(int((n1 + n2 + n3 + n4 + n5)%10))
