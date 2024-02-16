import sys
from collections import deque

input = sys.stdin.readline
n, m, r = map(int,input().split())
visited = [0 for _ in range(n+1)]
graph = [[] for _ in range(n+1)]
cnt = 0

for i in range(m):
    n1,n2 = map(int,input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)

q = deque([r])

while q:
    node = q.popleft()
    if visited[node]:
        continue
    cnt+=1
    visited[node] = cnt
    for next in sorted(graph[node],reverse=True):
        if visited[next] == 0:
            q.append(next)

for i in visited[1:]:
    print(i)