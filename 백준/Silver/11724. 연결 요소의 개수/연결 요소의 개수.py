from collections import deque
# 6 8
# 1 2
# 2 5
# 5 1
# 3 4
# 4 6
# 5 4
# 2 4
# 2 3

# def dfs(v,graph,visited):
#     stack = deque([v])

#     while stack:
#         v = stack.pop()
#         visited[v] = True
#         for node in graph[v]:
#             if not visited[node]:
#                 stack.append(node)

def dfs(v,graph,visited):
    visited[v] = True
    for node in graph[v]:
        if not visited[node]:
            dfs(node,graph,visited)

N,E = map(int,input().split())
cnt = 0

graph = [[] for _ in range(N+1)]
visited = [False for _ in range(N+1)]

for _ in range(E):
    n1,n2 = map(int,input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)

# print(graph)

for i in range(1,N+1):
    if visited[i]:
        continue
    cnt += 1
    dfs(i,graph,visited)

print(cnt)