import sys
input = sys.stdin.readline

k = int(input())
stack = []
for c in range(k):
    n = int(input())
    if n == 0:
        stack.pop()
    else:
        stack.append(n)

print(sum(stack))