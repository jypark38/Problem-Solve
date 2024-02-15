import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

def dfs(graph, visited, start, prev):
    global record
    record[0] += 1
    
    visited.append(start)
    for c in graph[start]:
        if prev == c:
            continue
        if not c in visited:
            record[1] += 1
            dfs(graph, visited, c, start)
        else:
            global flag
            flag = 0

cnt = 0
while True:
    v,e = map(int,input().split())
    cnt = cnt +1
    if(v==0 and e == 0):
        break
    else:
        graph = [[] for _ in range(v+1)]
        visited = []
        for _ in range(e):
            v1, v2 = map(int,input().split())
            graph[v1].append(v2)
            graph[v2].append(v1)
        T = 0
        for start in range(1,v+1):
            flag = 1
            record = [0,0]
            if not start in visited:
                dfs(graph,visited,start,0)
                if record[0] == record[1]+1 and flag:
                    T+=1
    
    if T>1:
        print(f"Case {cnt}: A forest of {T} trees.")
    elif T==1:
        print(f"Case {cnt}: There is one tree.")
    else:
        print(f"Case {cnt}: No trees.")

