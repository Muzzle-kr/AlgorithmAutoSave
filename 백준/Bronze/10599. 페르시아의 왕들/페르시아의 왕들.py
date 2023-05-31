while True:
    birth_min, birth_max, death_min, death_max = map(int, input().split())
    
    if birth_max == 0 and death_max == 0 and death_min == 0 and birth_min == 0:
        break

    print(death_min-birth_max, death_max-birth_min)