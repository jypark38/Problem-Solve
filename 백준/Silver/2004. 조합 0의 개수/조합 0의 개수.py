import math
n,m = map(int,input().split())

def factorial_cnt(n,t):
    cnt = 0
    while n:
        cnt += n//t
        n //= t
    return cnt

print(min((factorial_cnt(n,2) - factorial_cnt(n-m,2) - factorial_cnt(m,2),(factorial_cnt(n,5) - factorial_cnt(n-m,5) - factorial_cnt(m,5)))))