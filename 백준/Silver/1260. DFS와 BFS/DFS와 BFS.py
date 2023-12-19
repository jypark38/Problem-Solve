from collections import deque
N,E,start = map(int,input().split())

graph= [[] for _ in range(N+1)]
dfs_visited= [False] + [False for _ in range(N)]
bfs_visited= [False] + [False for _ in range(N)]

for i in range(E):
    n1,n2 = map(int,input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)

for i in range(1,N+1):
    graph[i].sort()

def dfs(v,graph,visited):
    visited[v] = True
    print(v,end=' ')

    for node in graph[v]:
        if not visited[node]:
            dfs(node,graph,visited)
    return

def bfs(v,graph,visited):
    queue = deque([v])
    visited[v] = True
    while queue:
        v = queue.popleft()
        print(v,end=' ')

        for node in graph[v]:
            if not visited[node]:
                queue.append(node)
                visited[node] = True


dfs(start,graph,dfs_visited)
print()
bfs(start,graph,bfs_visited)
