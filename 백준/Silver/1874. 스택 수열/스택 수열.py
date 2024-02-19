import sys
# input = sys.stdin.readline

n = int(input())
stack = []
answer = []
count = 1
for i in range(1,n+1):
    num = int(input())

    while count <= num:
        stack.append(count)
        answer.append('+')
        count+=1
    if stack[-1] == num:
        stack.pop()
        answer.append('-')
    else:
        break

if len(stack):
    print('NO')
else:
    for c in answer:
        print(c)