import math
import itertools as t

T = int(input())

for i in range(T):
    inp = list(map(int,input().split()))
    comb = t.combinations(inp[1:],2)
    answer = 0
    
    for (a,b) in comb:
        answer += math.gcd(a,b)
    print(answer)
        
