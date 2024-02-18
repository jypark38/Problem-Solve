import heapq
import sys
input = sys.stdin.readline
INF = sys.maxsize

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    n1,n2,cost = map(int,input().split())
    graph[n1].append((n2,cost))
start, end = map(int,input().split())

def dijkstra(start):
    q = []
    dist = [INF for _ in range(n+1)]
    dist[start] = 0
    heapq.heappush(q,(dist[start],start))

    while q:
        distance, node = heapq.heappop(q)

        if distance > dist[node]:
            continue

        for next, n_cost in graph[node]:
            new_cost = n_cost + distance
            if new_cost < dist[next]:
                dist[next] = new_cost
                heapq.heappush(q,(new_cost, next))
    return dist

result = dijkstra(start)
print(result[end])