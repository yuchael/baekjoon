import sys
sys.setrecursionlimit(10**6)

def dfs(x, y):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    graph[y][x] = -1
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if (0 <= nx < m) and (0 <= ny < n) and graph[ny][nx] == 1:
            dfs(nx, ny)
    
    
T = int(input())

for _ in range(T):
    count = 0
    m, n, k = map(int, input().split())
    graph = [[0 for _ in range(m)] for _ in range(n)]
    
    for _ in range(k):
        x, y = map(int, input().split())
        graph[y][x]= 1
    
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                dfs(j, i)
                count += 1
    print(count)
                