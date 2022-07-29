music = list(map(int, input().split()))
previous_scale = 0
ascending = []
descending = []

for idx, i in enumerate(music):
    if idx == 0:
        previous_scale = i
    else:
        if i - previous_scale == 1:
            ascending.append(i)
        elif i - previous_scale == -1:
            descending.append(i)
        previous_scale = i

# print(f'ascending = {ascending}')
# print(f'descending = {descending}')
if len(ascending) == 7:
    print("ascending")
elif len(descending) == 7:
    print("descending")
else:
    print("mixed")