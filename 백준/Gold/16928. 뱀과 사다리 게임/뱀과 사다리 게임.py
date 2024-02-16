from collections import deque

n,m = map(int,input().split())

ladder = dict()
snake = dict()

for _ in range(n):
    x,y = map(int,input().split())
    ladder[x] = y
for _ in range(m):
    x,y = map(int,input().split())
    snake[x] = y

dx = [1,2,3,4,5,6]

graph = [0]*101

q = deque([1])

while q:
    v = q.popleft()
    for i in dx:
        nv = v+i
        if 1<= nv <=100:
            if nv in ladder:
                nv = ladder[nv]
            if nv in snake:
                nv = snake[nv]
            if graph[nv] == 0:
                graph[nv] = graph[v] + 1
                q.append(nv)

print(graph[100])