def convertToBinary(value, n):
    value = int(value)
    result = ""
    
    while value > 1:
        result = str(value % 2) + result
        value = value // 2
    
    result = str(value) + result
    
    if len(result) < n:
        for i in range(n - len(result)):
            result = "0" + result
    return result


def solution(n, arr1, arr2):
    
    result = []
    binary1 = [convertToBinary(i, n) for i in arr1]
    binary2 = [convertToBinary(i, n) for i in arr2]
    # print(result)
    for i in range(n):
        a = binary1[i]
        b = binary2[i]
        structure = ""
        for j in range(n):
            if a[j] == "1" or b[j] == "1":
                structure += "#"
            else:
                structure += " "
        result.append(structure)    
    return result