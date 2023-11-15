word = input()
word = word.replace("XXXX", "AAAA").replace("XX", "BB")

if word.count("X") > 0:
    print(-1)
else:
    print(word)