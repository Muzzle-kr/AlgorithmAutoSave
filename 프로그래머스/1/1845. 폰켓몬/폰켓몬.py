def solution(nums):
    dict = {}
    
    for n in nums:
        dict[n] = 1
    
    if len(dict) > len(nums) // 2:
        return len(nums) // 2
    else:
        return len(dict)