n = int(input())
switch = [0] + list(map(int, input().split()))

def boy_change_switch(num):
    idx = 1
    # 숫자의 배수에 존재하는 스위치 바꿔주기
    while num * idx <= len(switch)-1:
        switch[num * idx] = 1 if switch[num * idx] == 0 else 0
        idx += 1
        
def girl_change_switch(num):
    
    # 자기꺼 먼저 바꿔주기
    switch[num] = 1 if switch[num] == 0 else 0
    idx = 1
    
    while 0 < num - idx and num + idx <= len(switch) - 1:
        
        if switch[num-idx] == switch[num+idx]:
            switch[num-idx] = 1 if switch[num-idx] == 0 else 0
            switch[num+idx] = 1 if switch[num+idx] == 0 else 0
            idx += 1
        else:
            break
    
for _ in range(int(input())):
    gen, num = map(int, input().split())
    
    if gen == 1:
        boy_change_switch(num)
    else:
        girl_change_switch(num)

idx = 0
for s in switch[1:]:
    print(s, end=" ")
    idx += 1
    
    if idx % 20 == 0:
        print()