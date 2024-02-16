from collections import deque
import sys
input = sys.stdin.readline

n,m = map(int,input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int,list(input().rstrip()))))

q = deque([(0,0)])

d = [(0,1),(0,-1),(1,0),(-1,0)]

while q:
    cx,cy = q.popleft()

    for dx,dy in d:
        nx,ny = cx+dx,cy+dy
        if 0 <= nx < n and 0 <= ny < m:                
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[cx][cy]+1
                q.append((nx,ny))

print(graph[n-1][m-1])