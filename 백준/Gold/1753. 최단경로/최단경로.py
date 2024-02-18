import heapq
import sys
input = sys.stdin.readline
INF = sys.maxsize

v,e = map(int,input().split())
k = int(input())

graph = [[] for _ in range(v+1)]
for _ in range(e):
    n1,n2,w = map(int,input().split())
    graph[n1].append((n2,w))

def dijkstra(start):
    q = []
    distances = [INF] * (v+1)
    distances[start] = 0
    heapq.heappush(q,(distances[start], start))

    while q:
        dist, curr = heapq.heappop(q)

        if dist > distances[curr]:
            continue
            
        for next, nw in graph[curr]:
            new_dist = dist + nw
            if new_dist < distances[next]:
                distances[next] = new_dist
                heapq.heappush(q,(new_dist, next))

    return distances
result = dijkstra(k)
for i in range(1,v+1):
    if result[i] == sys.maxsize:
        print('INF')
    else:
        print(result[i])