sentence = input()
result = ""

# 괄호는 순서를 보장해야함.
# 괄호가 아닌 것들은 순서를 변경해야함

def reverse_string(s):
    return "".join(list(reversed(list(s))))

tmp = ""
for s in sentence:
    
    if s == "<":
        if tmp != "":
            result += reverse_string(tmp)
        tmp = s
    elif s == ">":
        result += tmp+s
        tmp = ""
    elif s == " ":
        if "<" in tmp:
            tmp += s
            continue
        
        if tmp != "":
            result += reverse_string(tmp)
            tmp = ""
        result += s
        
    else:
        tmp += s

if tmp != "":
    result += reverse_string(tmp)
print(result)