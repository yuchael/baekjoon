import heapq

def solution(n, edge):
    answer = 0
    INF = int(1e9)
    q = []
    
    graph = [[] for _ in range(n + 1)]
    
    distance = [INF] * (n + 1)
    distance[1] = 0
    
    heapq.heappush(q, (0, 1))
    
    for e in edge:
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])
        
    while q:
        dist, cur = heapq.heappop(q)
        
        if distance[cur] < dist:
            continue
            
        for nxt in graph[cur]:
            if distance[nxt] > dist + 1:
                distance[nxt] = dist + 1
                heapq.heappush(q, (dist + 1, nxt))
    
    max_dist = 0
    for d in distance:
        if d != INF and d > max_dist:
            max_dist = d
            
    for d in distance:
        if d == max_dist:
            answer += 1
            
    return answer