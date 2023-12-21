import sys
sys.setrecursionlimit(111111)

def dfs(node,graph,cycle,visited):
    visited[node] = True
    cycle.append(node)
    next = graph[node]

    if visited[next]:
        if next in cycle:
            return len(cycle[cycle.index(next):])
        return 0
    else:
        return dfs(next,graph,cycle,visited)
        
t = int(input())
for case in range(t):
    n = int(input())
    graph = [0] + list(map(int,input().split()))
    visited = [False for _ in range(n+1)]
    result = n

    for i in range(1,n+1):
        if not visited[i]:
            result -= dfs(i,graph,[],visited)
    print(result)