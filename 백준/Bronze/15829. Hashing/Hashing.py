from string import ascii_lowercase
n = int(input())
word = input()
sum = 0
ascii = sorted(ascii_lowercase)

for idx, w in enumerate(word):
    sum += (ascii.index(w) + 1) * (31 ** idx)

print(sum % 1234567891)