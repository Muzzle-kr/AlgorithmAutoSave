N = int(input())

edges = []
total_people = 0
for _ in range(N):
    village, people = map(int, input().split())
    total_people += people
    edges.append((village, people))
    
edges.sort()

people_cnt = 0

for village, people in edges:
    people_cnt += people
    
    if people_cnt >= total_people / 2:
        print(village)
        break