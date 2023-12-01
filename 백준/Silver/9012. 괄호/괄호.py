import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    s = input()
    stack = []
    answer = 'YES'

    for c in s:
        if c == ')' and len(stack) == 0:
            answer = 'NO'
            break
        if c == '(':
            stack.append(c)
        elif c==')':
            stack.pop()

    if len(stack) != 0:
        answer = 'NO'
    
    print(answer)