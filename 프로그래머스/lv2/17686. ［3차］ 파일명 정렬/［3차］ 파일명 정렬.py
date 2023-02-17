def solution(files):
    answer = []
    
    # 파일을 3분류로 분리
    newFiles = []
    
    for i in files:
        head = ''
        number = ''
        tail = ''
        onTail = False
        for j in i:
            if j.isdigit() and len(number) < 5 and not onTail:
                    number += j
            elif len(number) > 0:
                onTail = True
                tail += j
            else:
                head += j

        newFiles.append([head, number, tail]) if tail != "" else newFiles.append([head, number])
    print(newFiles)
    answer = [ "".join(i[0]+i[1]+i[2]) if len(i) > 2  else "".join(i[0]+i[1]) for i in sorted(newFiles, key = lambda x: (x[0].lower(), int(x[1]))) ]
    return answer