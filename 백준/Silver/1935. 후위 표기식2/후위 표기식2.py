import sys
input = sys.stdin.readline

k = int(input())
s = list(input().rstrip())
stack = []
idx = {}
for c in s:
    if c.isalpha() and not c in idx:
        idx[c] = int(input())
for c in s:
    if c in '+-*/':
        a = stack.pop()
        b = stack.pop()
        if c == '+':
            result = a+b
        if c == '-':
            result = b-a
        if c == '*':
            result = a*b
        if c == '/':
            result = b/a
        stack.append(result)
    else:
        ch = idx[c]
        stack.append(ch)

print(f"{stack[-1]:0.2f}")