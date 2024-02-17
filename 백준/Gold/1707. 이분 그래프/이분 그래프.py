import sys
from collections import deque
input = sys.stdin.readline

def bfs(v):
    q = deque([v])
    visited[v] = 1
    while q:
        c = q.popleft()

        for i in graph[c]:
            if visited[i] == visited[c]:
                return 0
            if visited[i] == 0:
                visited[i] = visited[c] * -1
                q.append(i)
    return 1

k = int(input())

for case in range(k):
    v,e = map(int,input().split())

    graph =[[] for _ in range(v+1)]
    visited = [0] * (v+1)

    for _ in range(e):
        n1,n2 = map(int,input().split())
        graph[n1].append(n2)
        graph[n2].append(n1)

    for i in range(1,v+1):
        if visited[i] == 0:
            flag = bfs(i)
        if flag == 0:
            break
    

    print("YES" if flag else "NO")