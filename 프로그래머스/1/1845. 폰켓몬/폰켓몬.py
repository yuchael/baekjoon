def solution(nums):
    n = len(nums)
    
    pocketmons = set(nums)
    
    if len(pocketmons) < n // 2:
        answer = len(pocketmons)
    else:
        answer = n // 2
    
    return answer