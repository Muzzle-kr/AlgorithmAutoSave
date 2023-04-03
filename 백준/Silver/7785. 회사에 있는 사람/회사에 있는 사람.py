from collections import defaultdict
time_card = defaultdict(int)

for _ in range(int(input())):
    name, status = input().split()
    
    if status == "enter":
        time_card[name] = 1
    else:
        time_card[name] = 0
        
for name in sorted([k for k, v in time_card.items() if v == 1 ], reverse=True):
    print(name)