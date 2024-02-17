import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
graph = [list(map(int,input().rstrip())) for _ in range(n)]

move = [[[0,0] for _ in range(m)] for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1,-1,0,0]

q = deque([(0,0,0)])
move[0][0][0] = 1

while q:
    cx,cy,break_cnt = q.popleft()

    if (cx,cy) == (n-1,m-1):
        break

    for i in range(4):
        nx, ny = cx+dx[i], cy+dy[i]
        if 0 <= nx < n and 0 <= ny < m:

            if graph[nx][ny] == 1 and break_cnt == 0:
                move[nx][ny][1] = move[cx][cy][0] + 1
                q.append([nx,ny,1])
            if graph[nx][ny] == 0 and move[nx][ny][break_cnt] == 0:
                move[nx][ny][break_cnt] = move[cx][cy][break_cnt] + 1
                q.append([nx,ny,break_cnt])

if(move[n-1][m-1][break_cnt]==0):
    print(-1)
else:
    print(move[n-1][m-1][break_cnt])