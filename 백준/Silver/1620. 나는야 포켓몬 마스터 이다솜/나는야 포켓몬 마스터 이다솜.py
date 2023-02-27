n, m = map(int, input().split())
pokemon = []
answer = []

for i in range(n):
    name = input()
    pokemon.append(name)

for i in range(m):
    a = input()
    if not a.isdigit():
        answer.append(pokemon.index(a)+1)
    else:
        answer.append(pokemon[int(a)-1])
    
for a in answer:
    print(a)
        