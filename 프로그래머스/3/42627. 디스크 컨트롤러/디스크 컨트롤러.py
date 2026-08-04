import heapq

def solution(jobs):
    jobs.sort()
    q = []
    
    current_time = 0
    total_time = 0
    idx = 0     # 아직 힙에 넣지 않은 인덱스
    cnt = 0     # 처리된 작업 수
    n = len(jobs)
    
    while cnt < n:
        
        while idx < n and jobs[idx][0] <= current_time:
            request_time, processing_time = jobs[idx]
            heapq.heappush(q, (processing_time, request_time))
            idx += 1
            
        if q:
            processing_time, request_time = heapq.heappop(q)
            
            current_time += processing_time
            total_time += current_time - request_time
            cnt += 1
            
        else:
            current_time = jobs[idx][0]          

    return total_time // n