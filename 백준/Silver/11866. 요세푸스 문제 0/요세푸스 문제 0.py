from collections import deque

n,p = map(int,input().split())
arr = deque([i+1 for i in range(n)])
answer = []
while len(arr):
    arr.rotate(-p+1)
    answer.append(str(arr.popleft()))

print("<",end='')
print(', '.join(answer),end='')
print(">",end='')