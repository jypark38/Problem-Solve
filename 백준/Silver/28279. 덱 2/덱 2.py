from collections import deque
import sys

n = int(input())
deq = deque([])
l = 0
for _ in range(n): 
    u = sys.stdin.readline().split()
    if u[0] == '1':
        deq.appendleft(int(u[1]))
        l+=1
    if u[0] == '2':
        deq.append(int(u[1]))
        l+=1
    if u[0] == '3':
        if l: 
            print(deq.popleft())
            l-=1
        else:
            print(-1)
    if u[0] == '4':
        if l: 
            print(deq.pop())
            l-=1
        else:
            print(-1)
    if u[0] == '5':
        print(l)
    if u[0] == '6':
        print(0 if l else 1)
    if u[0] == '7':
        if l: 
            print(deq[0])
        else:
            print(-1)
    if u[0] == '8':
        if l: 
            print(deq[-1])
        else:
            print(-1)
