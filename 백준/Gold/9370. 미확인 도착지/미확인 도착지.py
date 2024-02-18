import heapq
import sys
INF = 1e9
input = sys.stdin.readline

T = int(input())

for case in range(T):
    n,m,t = map(int,input().split())
    s,g,h = map(int,input().split())
    graph = [[] for _ in range(n+1)]
    goal = []
    for i in range(m):
        n1,n2,d = map(int,input().split())
        graph[n1].append((n2,d))
        graph[n2].append((n1,d))

    for i in range(t):
        goal.append(int(input()))

    def dijkstra(start):

        q = []
        distance = [INF] * (n+1)
        distance[start] = 0
        heapq.heappush(q,(0,start))
        
        while q:
            dist, curr = heapq.heappop(q)
            if dist > distance[curr]:
                continue

            for next, next_dist in graph[curr]:
                new_dist = next_dist+dist
                if new_dist < distance[next]:
                    distance[next] = new_dist
                    heapq.heappush(q,(distance[next],next))

        return distance

    arr1 = dijkstra(s)
    arr2 = dijkstra(g)
    arr3 = dijkstra(h)
    result = []

    for i in goal:
        if arr1[g]+arr2[h]+arr3[i] == arr1[i] or arr1[h]+arr3[g]+arr2[i] == arr1[i]:
            result.append(i)

    print(*sorted(result))