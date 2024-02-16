from collections import deque
import sys

# input = sys.stdin.readline

def bfs(x,y):
    q = deque([(x,y)])
    graph[x][y] = 0
    d = [(0,1),(0,-1),(1,0),(-1,0)]
    while q:
        cx, cy = q.popleft()
        graph[cx][cy] = 0

        for dx,dy in d:
            nx, ny = cx+dx, cy+dy
            if 0<= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 1 and not (nx,ny) in q:
                    q.append((nx,ny))


t = int(input())
for case in range(t):
    m,n,k = map(int,input().split())

    graph = [[0 for _ in range(m)] for __ in range(n)]

    for _ in range(k):
        x,y = map(int,input().split())
        graph[y][x] = 1
    cnt = 0
    

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                bfs(i,j)
                cnt += 1

    print(cnt)