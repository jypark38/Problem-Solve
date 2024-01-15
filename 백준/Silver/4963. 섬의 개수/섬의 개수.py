import sys

sys.setrecursionlimit(10000000)

def dfs(x,y):
    if not (0 <= x < m):
        return False
    if not (0 <= y < n):
        return False
    
    if graph[x][y] == 1:
        graph[x][y] = 0
        for i in range(8):
            dfs(x+dx[i],y+dy[i])
        return True
    
    return False

while True:
    n,m = map(int,input().split())
    
    if n == 0 and m ==0:
        break

    dx = [-1,0,1,-1,1,-1,0,1]
    dy = [-1,-1,-1,0,0,1,1,1]

    graph = []

    for _ in range(m):
        graph.append(list(map(int,input().split())))
    cnt = 0
    for i in range(m):
        for j in range(n):
            if(dfs(i,j)):
                cnt+=1
    print(cnt)
