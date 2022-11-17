def convertToNumber(s):
    num = 0
    if s == "-": num = 0
    elif s == "\\": num = 1
    elif s == "(": num = 2
    elif s == "@": num = 3
    elif s == "?": num = 4
    elif s == ">": num = 5
    elif s == "&": num = 6
    elif s == "%": num = 7
    elif s == "/": num = -1
    return num

while True:
    string = input()
    length = len(string)
    
    if string == '#':
        break
    sum = 0
    for idx, s in enumerate(string):
        sum += convertToNumber(s) * pow(8, length - idx - 1)
    
    print(sum)