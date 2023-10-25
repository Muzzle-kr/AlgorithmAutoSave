S = input()
length = len(S)
hash = {}

for i in range(1, length+1):
    for j in range(length):
        hash[S[j:j+i]] = 1

print(len(hash))