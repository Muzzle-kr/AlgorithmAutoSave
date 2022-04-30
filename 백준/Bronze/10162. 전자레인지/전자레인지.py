a = 300
b = 60
c = 10

t = int(input())
answer = []

if t % c != 0:
    print(-1)
else:
    answer.append(t // a)
    answer.append(t % a // b)
    answer.append(t % a % b // c)

print(*answer, sep=" ")