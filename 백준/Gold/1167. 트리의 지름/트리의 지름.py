import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

def dfs(root,v,dist):
    for idx in range(len(graph[v])):
        child = graph[v][idx]
        d = weight[v][idx]
        if dist[child] == 0 and child != root:
            dist[child] = dist[v] + d
            dfs(root,child,dist)

v = int(input())

graph = [[] for _ in range(v+1)]
weight = [[] for _ in range(v+1)]
dist = [0 for _ in range(v+1)]
dist2 = [0 for _ in range(v+1)]

for i in range(v):
    inp = list(map(int,input().split()))
    node = inp[0]
    arr = inp[1:-1]
    for idx in range(0,len(arr),2): 
        graph[node].append(arr[idx])
        weight[node].append(arr[idx+1])


dfs(1,1,dist)

start = dist.index(max(dist))

dfs(start,start,dist2)

print(max(dist2))