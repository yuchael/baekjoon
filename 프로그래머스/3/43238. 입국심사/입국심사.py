def solution(n, times):
    answer = 0
    
    min_time = 0
    max_time = min(times) * n
    
    while min_time <= max_time:
        mid = (min_time + max_time) // 2
        
        sum = 0
        for t in times:
            sum += mid // t
        
        if sum < n:
            min_time = mid + 1
        else:
            answer = mid
            max_time = mid - 1    
    
    return answer