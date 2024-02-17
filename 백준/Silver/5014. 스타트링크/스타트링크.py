import sys
from collections import deque
input = sys.stdin.readline

f,s,g,u,d = map(int,input().split())

graph = [-1] * (f+1)

q = deque([s])
graph[s] = 0

while q:
    c = q.popleft()
    if c == g:
        break

    for ds in [u,-d]:
        next = c + ds

        if not (1 <= next <= f):
            continue
        if graph[next] == -1:
            graph[next] = graph[c]+1
            q.append(next)


if graph[g] == 0:
    print(0)
elif graph[g] != -1:
    print(graph[g])
else:
    print('use the stairs')