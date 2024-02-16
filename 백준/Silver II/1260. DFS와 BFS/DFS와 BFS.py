from collections import deque
import sys
input = sys.stdin.readline

def dfs(node):
    visited_dfs.append(node)

    for child in sorted(graph[node]):
        if not child in visited_dfs:
            dfs(child)

n,m,v = map(int,input().split())

graph = [[] for _ in range(n+1)]
visited_dfs = []
visited_bfs = []

for _ in range(m):
    n1, n2 = map(int,input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)

dfs(v)

q = deque([v])
while q:
    node = q.popleft()
    if node in visited_bfs:
        continue
    visited_bfs.append(node)
    for child in sorted(graph[node]):
        if not child in visited_bfs:
            q.append(child)
print(*visited_dfs)
print(*visited_bfs)