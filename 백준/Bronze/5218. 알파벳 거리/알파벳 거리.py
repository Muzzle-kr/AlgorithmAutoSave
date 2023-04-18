import string
ascii_arr = list(string.ascii_uppercase)

def print_distances(arr):
    print("Distances:", *arr)
    
for _ in range(int(input())):
    a, b = input().split()
    arr = []
    
    for i in range(len(a)):
        distance = ascii_arr.index(b[i]) - ascii_arr.index(a[i])
        if distance < 0:
            arr.append(26 + distance)
        else:
            arr.append(distance)
    
    print_distances(arr)