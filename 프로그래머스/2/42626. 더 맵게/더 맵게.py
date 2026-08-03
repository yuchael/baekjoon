import heapq

def solution(scoville, K):
    q = []
    
    for food in scoville:
        heapq.heappush(q, food)
    
    first = heapq.heappop(q)
    count = 0
    while q and first < K:
        second = heapq.heappop(q)
        heapq.heappush(q, (first + second * 2))
        count += 1
        first = heapq.heappop(q)
    
    if first < K:
        return -1
        
    answer = count
    return answer