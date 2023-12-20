def dfs(v,graph,visited):
    if visited[v]:
        return
    
    visited[v] = True
    next = graph[v]
    if not visited[next]:
        dfs(next,graph,visited)

t = int(input())
for case in range(t):
    v = int(input())

    visited = [False for _ in range(v+1)]
    graph = [0] + list(map(int,input().split()))
    cnt = 0

    for i in range(1,v+1):
        if not visited[i]:
            dfs(i,graph,visited)
            cnt+=1

    print(cnt)