for a in range(1, 101):
    result = a ** 3
    
    for i in range(2, 99):
        for j in range(i + 1, 98):
            for k in range(j + 1, 97):
                sum = (i * i * i) + (j * j * j) + (k * k * k)
                if result == sum:
                    print(f'Cube = {a}, Triple = ({i},{j},{k})')