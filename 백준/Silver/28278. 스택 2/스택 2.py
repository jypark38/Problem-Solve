import sys
input = sys.stdin.readline

T = int(input())
stack = []
length = 0

for _ in range(T):
    q = list(map(int,input().split()))
    if q[0] == 1:
        stack.append(q[1])
        length += 1
    if q[0] == 2:
        if not length:
            print(-1)
        else:
            print(stack.pop())
            length-=1
    if q[0] == 3:
        print(length)
    if q[0] == 4:
        if not length:
            print(1)
        else:
            print(0)
    if q[0] == 5:
        if not length:
            print(-1)
        else:
            print(stack[-1])