import heapq
import sys
input = sys.stdin.readline
INF = sys.maxsize

cnt = 0
while True:
    n = int(input())
    if n == 0:
        break
    cnt += 1
    graph = []
    for i in range(n):
        graph.append(list(map(int,input().split())))

    def dijkstra(sx,sy):
        q=[]
        distances = [[INF for _ in range(n)] for _ in range(n)]
        distances[sx][sy] = graph[sx][sy]
        heapq.heappush(q,(distances[sx][sy],sx,sy))

        while q:
            dist , cx, cy = heapq.heappop(q)

            if dist > distances[cx][cy]:
                continue

            for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                nx, ny = cx+dx, cy+dy
                
                if not (0<= nx < n and 0 <= ny < n):
                    continue

                new_dist = dist + graph[nx][ny]
                if new_dist < distances[nx][ny]:
                    distances[nx][ny] = new_dist
                    heapq.heappush(q,(new_dist,nx,ny))

        return distances

    result = dijkstra(0,0)

    print(f"Problem {cnt}: {result[-1][-1]}")