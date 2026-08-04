def solution(citations):
    answer = 0
    
    citations.sort(reverse=True)
    
    i = 0
    while i <= len(citations) - 1 and citations[i] >= i + 1:
        i += 1
    
    return i