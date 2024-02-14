from collections import deque

m,n = map(int,input().split())
q = deque([])
graph = []
dx = [0,0,-1,1]
dy = [1,-1,0,0]

for i in range(m):
    arr = list(input())
    graph.append(arr)

q.append((0,0))

while q:
    x,y = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i] 
        
        if 0 <= nx < m and 0 <= ny < n:
            if int(graph[nx][ny]) == 1:
                graph[nx][ny] = int(graph[x][y]) + 1
                q.append((nx,ny))

print(graph[m-1][n-1])