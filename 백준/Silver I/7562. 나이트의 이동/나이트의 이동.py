from collections import deque
import sys
input = sys.stdin.readline

t = int(input())

for iter in range(t):
    l = int(input())

    sx,sy = map(int,input().split())
    ex,ey = map(int,input().split())

    graph = [[0 for i in range(l)] for j in range(l)]

    q = deque([(sx,sy)])

    d = [(-1,-2),(-2,-1),(-1,2),(-2,1),(1,-2),(2,-1),(1,2),(2,1)]

    while q:
        cx, cy = q.popleft()
        
        if cx == ex and cy == ey:
            break

        for dx,dy in d:
            nx, ny = cx+dx, cy+dy

            if 0 <= nx <l and 0 <= ny < l:
                if graph[nx][ny] == 0:
                    graph[nx][ny] = graph[cx][cy] + 1
                    q.append((nx,ny))

    print(graph[ex][ey])