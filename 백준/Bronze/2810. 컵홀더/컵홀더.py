N = int(input())
arr = list(input())

print(min(N - ((arr.count("L")//2) - 1), N))