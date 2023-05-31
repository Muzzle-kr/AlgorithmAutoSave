b_x, b_y = map(int, input().split())
d_x, d_y = map(int, input().split())
j_x, j_y = map(int, input().split())


d_distance = abs(j_x - d_x) + abs(j_y - d_y)
b_distance = min(abs(j_x - b_x), abs(j_y - b_y)) + (max(abs(j_x - b_x), abs(j_y - b_y)) - min(abs(j_x - b_x), abs(j_y - b_y)))

if d_distance > b_distance:
    print("bessie")
elif d_distance < b_distance:
    print("daisy")
else:
    print("tie")