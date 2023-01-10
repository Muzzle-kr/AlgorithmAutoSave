import re

def solution(s):
    pattern = '[{/d}]+'
    a = re.split(pattern, s)
    answer = []
    result = []
    for idx in range(len(a)):
        if a[idx] != '' and (a[idx+1] == '' or a[idx+1] == ',') :
            subset = a[idx].split(",")
            answer.append(subset)
    
    answer.sort(key=lambda x: len(x))
    
    
    for i in answer:
        for j in i:
            j = int(j)
            if j not in result:
                result.append(int(j))
    
    return result