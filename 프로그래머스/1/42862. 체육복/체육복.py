def solution(n, lost, reserve):
    
    lost, reserve = list(set(lost) - set(reserve)), list(set(reserve) - set(lost))
    
    lost.sort()
    reserve.sort()
    
    l = len(lost)
    answer = n - l
    
    for c in reserve:
        if c - 1 in lost:
            lost.remove(c - 1)
            answer += 1
        elif c + 1 in lost:
            lost.remove(c + 1)
            answer += 1
    
    return answer