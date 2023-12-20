from collections import deque

def bfs(v,graph,visited,color):
        q = deque([v])
        color[v] = 1

        while q:
            node = q.popleft()
            next_color = color[node]*-1
            visited[node] = True

            for next in graph[node]:
                if not visited[next]:
                    color[next] = next_color
                    visited[next] = True
                    q.append(next)
                elif color[next] == color[node]:
                    return 0
        return 1

t = int(input())

for case in range(t):
    v,e = map(int,input().split())
    graph = [[] for _ in range(v+1)]
    visited = [False for _ in range(v+1)]
    color = [0 for _ in range(v+1)]
    for _ in range(e):
        n1, n2 = map(int,input().split())
        graph[n1].append(n2)
        graph[n2].append(n1)

    flag = 1

    for i in range(1,v+1):
        if not visited[i]:
            if not bfs(i,graph,visited,color):
                flag=0
                break
    
    print('YES' if flag else 'NO')