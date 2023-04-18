vowel = ["a", "e", "i", "o", "u"]
string = input().strip()
print(len([c for c in string if c in vowel]))