import sys
input = sys.stdin.readline

def dfs(node):
    global cnt
    visited[node] = True

    for child in graph[node]:
        if not visited[child]:
            dfs(child)
            cnt += 1

n = int(input())
m = int(input())
cnt = 0

graph = [[] for _ in range(n+1)]
visited = [0 for _ in range(n+1)]

for _ in range(m):
    n1,n2 = map(int,input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)
dfs(1)
print(cnt)