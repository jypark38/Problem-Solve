from collections import deque
import sys
import copy

n = int(sys.stdin.readline())
deq = deque(map(int,input().split()))
arr = deque([i+1 for i in range(n)])
answer = []
for i in range(1,n+1):
    a = deq[0]
    deq.popleft()
    answer.append(arr.popleft())
    if(a>0):
        r = -a+1
    else:
        r = -a
    deq.rotate(r)
    arr.rotate(r)

print(*answer)