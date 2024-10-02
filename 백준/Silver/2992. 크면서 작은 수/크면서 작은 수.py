answer = set()
n = int(input())

string = list(str(n))

def bt(number_string, index, visited):
    if index == len(string):
        answer.add(int(number_string))
        return
    
    for j in range(len(string)):
        if not visited[j]:
            visited[j] = True
            bt(number_string + string[j], index + 1, visited)
            visited[j] = False
    return

visited = [False] * len(string)

for i in range(len(string)):
    visited[i] = True
    bt(string[i], 1, visited)
    visited[i] = False


answer = list(answer)
answer.sort()
position = answer.index(n)

if len(answer) > position + 1:
    print(answer[position + 1])
else:
    print(0)