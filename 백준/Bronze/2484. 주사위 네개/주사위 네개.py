res_li=[]
for _ in range(int(input())):
    li = list(map(int,input().split()))
    #set은 집합으로 중복된 숫자를 없앨 수 있다.
    #set의 길이로 case1, 2와3, 4,5를 나눌 수 있다.
    st = len(set(li))
    #숫자가 다 같으면 set에 하나의 값이 있다.
    if st == 1:
        #리스트의 아무 값이나 골라서 넣는다
        res_li.append(50000+li[0]*5000)
    
    #1113,1133 같이 case 2 3 번의 경우
    elif st == 2:
        #기준을 일단 제일 큰 값으로 잡아 봤음
        #set이 아닌 list안에 개수를 파악하여 case를 나눠 줌
        count = li.count(max(li))
        
        #case 2큰 값이 하나라면 다른 값(작은 값으로 구분)이 3개 라는 뜻
        if count ==1:
            res_li.append(min(li)*1000 + 10000)
        #case 2
        elif count ==3:
            res_li.append(max(li)*1000 + 10000)
        
        #case 3 위에서 이미 set의 길이가 2라는 것을 파악하여
        #같은 숫자가 2개 2개라는 것을 알 수 있음
        elif count ==2:
            res_li.append(max(li)*500+ min(li)*500 + 2000)
    
    #case 4 길이가 3이면 집합(1233) -> 123 
    elif st == 3:
        #리스트에서 하나씩 골라
        for p in li:
            #개수가 2개인 것을 찾는다.
            if li.count(p) == 2:
                res_li.append(p*100+1000)
                break
    #case 5
    else:
        res_li.append(max(li)*100)
print(max(res_li))