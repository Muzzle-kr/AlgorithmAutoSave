n, m, w = map(int, input().split())

share = w // m
rest = w % m

print(share, rest)