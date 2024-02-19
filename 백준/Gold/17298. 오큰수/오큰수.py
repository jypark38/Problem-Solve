n = int(input())
nums = list(map(int,input().split()))
stack = []
idx_stack = []
answer = [-1]*n

for i in range(n):
    while stack:
        if stack[-1] < nums[i]:
            stack.pop()
            answer[idx_stack.pop()] = nums[i]
        else:
            break
    stack.append(nums[i])
    idx_stack.append(i)

print(*answer)