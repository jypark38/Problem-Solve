import sys

n = int(sys.stdin.readline())

if (n%2 == 1):
        print(0)
else:
    dp = [0,0,3,0] + [0 for _ in range(4,n+1)]

    for i in range(4,n+1,2):
        for j in range(2,i,2):
            if j==2:
                dp[i] += dp[i-j]*3
            else:
                 dp[i] += dp[i-j]*2
        dp[i]+=2
    print(dp[n])