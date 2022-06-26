repeat = int(input())

for i in range(repeat):
    n1, n2 = map(int, input().split())
    sum = n1 + n2

    print('Case %d: %d' % (i + 1, sum))
