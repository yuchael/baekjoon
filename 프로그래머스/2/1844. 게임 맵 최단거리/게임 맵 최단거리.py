from collections import deque

def solution(maps):    
    n = len(maps)
    m = len(maps[0])
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    visited = [[False] * m for _ in range(n)]
    visited[0][0] = True
    
    q = deque([(0, 0, 1)])
    
    while q:
        x, y, dist = q.popleft()
        
        if x == n - 1 and y == m - 1:
            return dist
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if maps[nx][ny] and not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx, ny, dist + 1))

    return -1