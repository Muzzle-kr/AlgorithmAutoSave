import math

day, night, height = map(int, input().split())
currentHeight = 0
past = 0

print(math.ceil((height - day) / (day - night)) + 1)