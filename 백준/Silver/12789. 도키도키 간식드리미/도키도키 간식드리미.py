from collections import deque

n = int(input())
arr = deque(list(map(int,input().split())))
stack = []
p = 1
answer = 'Nice'
while arr:
    if p == arr[0]:
        arr.popleft()
        p+=1
    else:
        if stack and stack[-1] < arr[0]:
            break
        stack.append(arr.popleft())
    while stack and stack[-1] == p:
        stack.pop()
        p+=1
if stack:
    print('Sad')
else:
    print('Nice')