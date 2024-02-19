n,k = map(int,input().split())
nums = list(input())
stack = []

for i in range(n):
    while stack and k>0 and stack[-1] < nums[i]:
        k-=1
        stack.pop()
        
    stack.append(nums[i])

while k:
    stack.pop()
    k-=1

print(''.join(stack))