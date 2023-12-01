import sys
queue = []
N = int(input())
size = 0
cnt = 0
for _ in range(N):
    s = sys.stdin.readline().split()
    if s[0] =='push':
        queue.append(int(s[1]))
        size += 1
    if s[0] =='pop':
        if size == 0:
            print(-1)
        else:
            print(queue[cnt])
            cnt+=1
            size -= 1
    if s[0] == 'size':
        print(size)
    if s[0] == 'empty':
        if size == 0:
            print(1)
        else :
            print(0)
    if s[0] == 'front':
        if size == 0:
            print(-1)
        else:
            print(queue[cnt])
    if s[0] == 'back':
        if size == 0:
            print(-1)
        else:
            print(queue[-1])

