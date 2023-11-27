A,B = map(int,input().split())
m = int(input())
nums = list(map(int,input().split()))
nums.reverse()

ten = 0

for i in range(m):
    ten += nums[i] * pow(A,i)

answer = []
while ten:
    ten,r = divmod(ten,B)
    answer.append(str(r))


print(' '.join(answer[::-1]))