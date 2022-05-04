word = input()
start = 0
end = len(word)-1

while start < end:
    # print(start, end)
    if word[start] != word[end]:
        print(0)
        exit()
    start += 1
    end -= 1
print(1)