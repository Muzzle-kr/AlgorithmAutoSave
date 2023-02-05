suffix_arr = []
word = input()
for i in range(len(word)):
    suffix_arr.append(word[i:])

for i in sorted(suffix_arr):
    print(i)


