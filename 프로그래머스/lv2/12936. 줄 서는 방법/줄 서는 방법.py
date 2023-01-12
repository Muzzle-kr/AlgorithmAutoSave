factorial = [0] * 21
factorial[1] = 1

for i in range(2, 21):
    factorial[i] = i * factorial[i - 1]

# print(factorial)
# [0, 1, 2, 6, 24, ....]
def solution(n, k):
    arr = [i + 1 for i in range(n)]
    length = n
    result = []
    k = k - 1
    while True:
        if length == 1:
            result.append(arr[0])
            break
        
        # print('--------------------------')
        # jump값만큼 앞자리 숫자가 변한다. 2
        jump = factorial[length-1]
        # print(f'jump: {jump}')
        
        # k를 jump로 나눈 몫 = 2
        
        share = k // jump
        # print(f'share: {share}')
        
        # 해당 share가 num이된다.
        num = arr[share]
        # print(f'num: {num}')
        # result에 num을 push
        result.append(num)
        
        # k만큼 돌아야한다..
        k = k % jump
        # print(f'k: {k}')

        # arr는 자기 자신이 아닌 것을 제외한 배열로 재할당
        arr = [i for i in arr if i != num]
        # print(f'arr: {arr}')
        
        length -= 1
    return result