import sys
from collections import deque
input = sys.stdin.readline

def bfs(x,y,color,visited):
    q = deque([(x,y)])
    visited[x][y] = 1

    while q:
        cx, cy = q.popleft()
        
        for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]:
            nx, ny = cx+dx, cy+dy

            if not (0 <= nx < n and 0 <= ny < n):
                continue
            if visited[nx][ny] == 0 and color == graph[nx][ny]:
                visited[nx][ny] = 1
                q.append((nx,ny))

    return

def bfs_(x,y,color,visited):
    q = deque([(x,y)])
    visited[x][y] = 1

    while q:
        cx, cy = q.popleft()
        
        for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]:
            nx, ny = cx+dx, cy+dy

            if not (0 <= nx < n and 0 <= ny < n):
                continue
            if visited[nx][ny] == 0:
                if color == 'B' and graph[nx][ny] == 'B':
                    visited[nx][ny] = 1
                    q.append((nx,ny))
                elif color != 'B' and graph[nx][ny] != 'B':
                    visited[nx][ny] = 1
                    q.append((nx,ny))

    return

n = int(input())

graph = []
for i in range(n):
    graph.append(list(input().rstrip()))

visited1 = [[0 for _ in range(n)] for _ in range(n)]
visited2 = [[0 for _ in range(n)] for _ in range(n)]

cnt1 = 0
cnt2 = 0

for i in range(n):
    for j in range(n):
        if visited1[i][j] == 0:
            bfs(i,j,graph[i][j],visited1)
            cnt1+=1
        if visited2[i][j] == 0:
            bfs_(i,j,graph[i][j],visited2)
            cnt2 += 1
print(cnt1, cnt2)