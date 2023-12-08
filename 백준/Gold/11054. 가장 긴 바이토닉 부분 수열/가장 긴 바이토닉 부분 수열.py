n = int(input())

arr = list(map(int,input().split()))

arr_r = [0] + list(reversed(arr))
arr = [0] + arr
dp = [0] + [1 for _ in range(n)]
dp2 = [0] + [1 for _ in range(n)]
result = []
for i in range(1,n+1):
    for j in range(1,i):
        if (arr[i]>arr[j]):
            dp[i] = max(dp[i],dp[j]+1)
    for j in range(1,i):
        if (arr_r[i]>arr_r[j]):
            dp2[i] = max(dp2[i], dp2[j]+1)

dp = dp[1:]
dp2 = dp2[1:][::-1]

for i in range(n):
    result.append(dp[i]+dp2[i]-1)

print(max(result))
