import math

T = int(input())

for i in range(T):
    inp = list(map(int,input().split()))
    n = inp[0]
    inp = inp[1:]
    s = list()
    for j in range(n):
        for k in range(j+1,n):
            s.append(math.gcd(inp[j],inp[k]))
    print(sum(s))