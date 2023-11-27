T = int(input())

for i in range(T):
    a,b = map(int,input().split())
    s = a*b
    while b != 0:
        a,b = b,a%b
    print(s//a)