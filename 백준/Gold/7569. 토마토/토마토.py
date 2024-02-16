from collections import deque
import sys
input = sys.stdin.readline


d = [(0,0,1),(0,0,-1),(1,0,0),(-1,0,0),(0,1,0),(0,-1,0)]

n,m,h = map(int,input().split())
q = deque([])
graph = []
for i in range(h):
    arr = []
    for j in range(m):
        arr.append(list(map(int,input().split())))
        for k in range(n):
            if arr[j][k] == 1:
                q.append((j,k,i))
    graph.append(arr)

while q:
    cx,cy,cz = q.popleft()

    for dx,dy,dz in d:
        nx,ny,nz = cx+dx,cy+dy,cz+dz
        if 0 <= nx < m and 0 <= ny < n and 0 <= nz < h:
            if graph[nz][nx][ny] == 0:
                graph[nz][nx][ny] = graph[cz][cx][cy] + 1
                q.append((nx,ny,nz))
answer=  0
flag = 1
for box in graph:
    if flag == 0:
        break
    for row in box:
        if 0 in row:
            answer = 0
            flag = 0
            break
        m = max(row)
        if m > answer:
            answer = m

print(answer-1)
