A, B = map(int, input().split())

arrofA = set(list(map(int, input().split())))
arrofB = set(list(map(int, input().split())))

result = sorted(list(arrofA - arrofB))

if len(result) == 0:
    print(0)
else:
    print(len(result))
    print(*result)