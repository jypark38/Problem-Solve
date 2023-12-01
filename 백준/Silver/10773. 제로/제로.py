import sys
input = sys.stdin.readline

T = int(input())
stack = []

for _ in range(T):
    i = int(input())
    if i == 0:
        stack.pop()
    else:
        stack.append(i)

print(sum(stack))