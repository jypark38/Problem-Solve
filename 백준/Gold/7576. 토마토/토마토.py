from collections import deque

m,n = map(int,input().split())
q = deque([])
graph = []
dx = [0,0,-1,1]
dy = [1,-1,0,0]

for i in range(n):
    arr = list(map(int,input().split()))
    graph.append(arr)
    for j in range(m):
        if(graph[i][j] == 1):
            q.append((i,j))

while q:
    x,y = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i] 
        
        if 0 <= nx < n and 0 <= ny < m:
            if graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                q.append((nx,ny))

m = 0
for i in range(n):
    if 0 in graph[i]:
        m = 0
        break
    mx = max(graph[i])
    if m < mx:
        m = mx
print(m-1)