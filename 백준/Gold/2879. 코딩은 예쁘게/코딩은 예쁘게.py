n = int(input())
now_tab = list(map(int, input().split()))
correct_tab = list(map(int, input().split()))

count = 0
condition = [0, 1, 2]
check = 0
while now_tab != correct_tab:
    for i in range(n):
        if now_tab[i] == correct_tab[i]:
            check = 0
        elif now_tab[i] > correct_tab[i]:
            if check != 1:
                count += 1
                now_tab[i] -= 1
                check = 1
            else:
                now_tab[i] -= 1
        else:
            if check != 2:
                count += 1
                now_tab[i] += 1
                check = 2
            else:
                now_tab[i] += 1
    check = 0

print(count)