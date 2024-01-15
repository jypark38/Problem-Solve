def dfs(x,y):
    global tmp
    if x<=-1 or x>=n or y <= -1 or y>= n:
        return False
    if graph[x][y] == 1:
        graph[x][y]=0
        tmp += 1
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y-1)
        dfs(x,y+1)
        return True
    return False

n = int(input())

graph = []
for i in range(n):
    graph.append(list(map(int,list(input()))))

result1 = 0
result2 = []

for i in range(n):
    for j in range(n):
        tmp = 0
        if dfs(i,j):
            result1+=1
            result2.append(tmp)
result2.sort()

print(result1)
for i in result2:
    print(i)
