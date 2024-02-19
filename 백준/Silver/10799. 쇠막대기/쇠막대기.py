s = input()

stack = []
sum = 0
idx = 0

s=s.replace('()','-')
for c in s:
    if c == '-':
        sum+=len(stack)
    if c == '(':
        stack.append('(')
    elif c == ')':
        stack.pop()
        sum+=1

print(sum)