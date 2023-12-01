from collections import deque
import sys

n = int(input())
q = deque([])
l = 0
for _ in range(n):
    u =  sys.stdin.readline().split()

    if(u[0] == 'push'):
        q.append(int(u[1]))
        l+=1
    if(u[0] == 'pop'):
        if not l :
            print(-1)
        else:
            print(q.popleft())
            l-=1
    if(u[0] == 'size'):
        print(l)
    if(u[0] == 'empty'):
        if not l :
            print(1)
        else:
            print(0)
    if(u[0] == 'front'):
        if not l :
            print(-1)
        else:
            print(q[0])
    if(u[0] == 'back'):
        if not l :
            print(-1)
        else:
            print(q[-1])