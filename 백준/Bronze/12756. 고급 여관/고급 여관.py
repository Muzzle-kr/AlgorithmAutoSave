a_attack, a_heart = map(int, input().split())
b_attack, b_heart = map(int, input().split())

while a_heart > 0 and b_heart > 0:
    a_heart -= b_attack
    b_heart -= a_attack

if a_heart <= 0 and b_heart <= 0:
    print("DRAW")
elif a_heart > b_heart:
    print("PLAYER A")
else:
    print("PLAYER B")