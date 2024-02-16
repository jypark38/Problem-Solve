import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
n, m, r = map(int,input().split())
visited = [0 for _ in range(n+1)]
graph = [[] for _ in range(n+1)]
cnt = 0

for i in range(m):
    n1,n2 = map(int,input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)

stack = [r]

while stack:
    node = stack.pop()
    if visited[node]:
        continue
    cnt += 1
    visited[node] = cnt
    # stack에 들어가니까 내림차순으로 방문할거면 오름차순으로 나열
    for next in sorted(graph[node]):
        if not visited[next]:
            stack.append(next)

for i in visited[1:]:
    print(i)