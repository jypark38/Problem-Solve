import sys
input = sys.stdin.readline

stack1 = list(input().rstrip())
stack2 = []
m = int(input())

for i in range(m):
    inp = input().split()
    if inp[0] == 'P':
        stack1.append(inp[1])
    elif inp[0] == 'L':
        if len(stack1) <= 0:
            continue
        stack2.append(stack1.pop())
    elif inp[0] == 'D':
        if len(stack2) <= 0:
            continue
        stack1.append(stack2.pop())
    elif inp[0] == 'B':
        if len(stack1) <= 0:
            continue
        stack1.pop()

print("".join(stack1+stack2[::-1]))
