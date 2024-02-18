from collections import deque
import sys
input = sys.stdin.readline

n,k = map(int,input().split())

graph = [0] * 100001

q = deque([n])

while q:
    c = q.popleft()

    if c == k:
        break

    for next in [c-1,c+1,c*2]:
        if not (0 <= next <= 100000):
            continue

        if graph[next] != 0:
            continue

        if next == c*2 and next != 0:
            graph[next] = graph[c]
            q.appendleft(next)
        else:
            graph[next] = graph[c]+1
            q.append(next)
            
print(graph[k])