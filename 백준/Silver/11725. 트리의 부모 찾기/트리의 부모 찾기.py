from collections import deque

n = int(input())
visited = [False for _ in range(n+1)]
answer = [0 for _ in range(n+1)]
graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

queue = deque([1])

while queue:
    node = queue.popleft()
    visited[node] = True

    for child in graph[node]:
        if visited[child] == False:
            visited[child] = True
            answer[child] = node
            queue.append(child)

for i in answer[2:]:
    print(i)