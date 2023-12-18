import sys

n = int(sys.stdin.readline())

if (n%2 == 1):
        print(0)
else:
    dp = [1,0,3,0] + [0 for _ in range(4,n+1)]

    for i in range(4,n+1,2):
        dp[i] += dp[i-2]*3
        for j in range(4,i+1,2):
            dp[i] += dp[i-j]*2
    print(dp[n])