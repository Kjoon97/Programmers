def solution(nums):
    dic = {x:1 for x in nums}
    if len(dic) >= len(nums)//2: 
        return len(nums)//2
    elif len(dic) < len(nums)//2:
        return len(dic)
