n = int(input())
graph = []

for _ in range(n):
    graph.append(list(map(int,list(input()))))

result = []

def dfs(graph,x,y):
    global cnt
    if x < 0 or x >= n:
        return False
    if y < 0 or y >= n:
        return False
    if graph[x][y] == 1:
        graph[x][y] = 0
        cnt += 1
        dfs(graph,x-1,y)
        dfs(graph,x+1,y)
        dfs(graph,x,y-1)
        dfs(graph,x,y+1)
        return True
    return False

for i in range(n):
    for j in range(n):
        cnt = 0
        if (dfs(graph,i,j)):
            result.append(cnt)

result.sort()
print(len(result))
for i in result:
    print(i)