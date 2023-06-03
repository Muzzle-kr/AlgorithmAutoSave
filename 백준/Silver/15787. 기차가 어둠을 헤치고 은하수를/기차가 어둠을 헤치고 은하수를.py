train_dict = set()
n, m = map(int, input().split())
train = [[0] * 20 for _ in range(n)]

for _ in range(m):
    order = list(map(int, input().split()))
    tn = order[1] - 1
    
    if order[0] == 1:
        train[tn][order[2]-1] = 1
    elif order[0] == 2:
        train[tn][order[2]-1] = 0
    elif order[0] == 3:
        for i in range(19, 0, -1):
            train[tn][i] = train[tn][i-1]
        train[tn][0] = 0
    else:
        for i in range(19):
            train[tn][i] = train[tn][i+1]
        train[tn][19] = 0
    
for i in range(n):
    if str(train[i]) not in train_dict:
        train_dict.add(str(train[i]))
    
print(len(train_dict))