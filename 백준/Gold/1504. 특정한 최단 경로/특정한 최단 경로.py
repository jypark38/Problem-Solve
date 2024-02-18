import heapq
import sys
input = sys.stdin.readline
INF = 1e9

v,e = map(int,input().split())

graph = [[] for _ in range(v+1)]
for _ in range(e):
    n1,n2,w = map(int,input().split())
    graph[n1].append((n2,w))
    graph[n2].append((n1,w))

n1, n2 = map(int,input().split())

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

result1 = dijkstra(1)
sToN1 = result1[n1]
sToN2 = result1[n2]

result2 = dijkstra(n1)
N1ToN2 = result2[n2]
N1ToE = result2[v]

N2ToE = dijkstra(n2)[v]


answer = min(sToN1+N1ToN2+N2ToE,sToN2+N1ToN2+N1ToE)

if answer >= INF:
    print(-1)
else:
    print(answer)