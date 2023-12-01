import sys
input = sys.stdin.readline


while True:
    s = input()
    if(s=='.\n'): 
        break
    stack = []
    answer = 'yes'

    for c in s:
        if (c==']' or c == ')') and len(stack) == 0:
            answer = 'no'
            break
        if c == '(' or c == '[':
            stack.append(c)
        elif c==')':
            if stack[-1] == '(':
                stack.pop()
            else:
                answer = 'no'
                break
        elif c ==']':
            if stack[-1] == '[':
                stack.pop()
            else:
                answer = 'no'
                break

    if len(stack) != 0:
        answer = 'no'
    
    print(answer)