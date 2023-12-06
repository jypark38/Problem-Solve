n = int(input())
arr = [0]
dp = [0 for _ in range(n+1)]

for _ in range(n):
    arr.append(int(input()))
dp[1] = arr[1]


for i in range(2,n+1):
    if i == 2:
        dp[i] = arr[i]+arr[i-1]
    else:
        dp[i] = max(arr[i] + dp[i-2], arr[i] + arr[i-1] + dp[i-3],dp[i-1])
    

print(dp[-1])