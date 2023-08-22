now = input()
next = input()

word = ""
cnt = 0

for w in next:
    if word + w in now:
        word += w
    else:
        word = w
        cnt += 1

print(cnt + 1)
