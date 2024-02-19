import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n = int(input())
mp,mf,ms,mv = map(int,input().split())
p = []
f = []
s = []
v = []
c = []
result=[]
min = 100000

for _ in range(n):
    pi,fi,si,vi,ci = map(int,input().split())
    p.append(pi)
    f.append(fi)
    s.append(si)
    v.append(vi)
    c.append(ci)

def back(depth,P,F,S,V,C,answer):
    global min
    global result
    if depth == n or C >= min:
        return
    answer.append(depth+1)
    P += p[depth]
    S += s[depth]
    F += f[depth]
    V += v[depth]
    C += c[depth]
    if P>=mp and F>=mf and S>=ms and V>=mv:
        if C < min:
            min = C
            result = list.copy(answer)


    back(depth+1,P,F,S,V,C,answer)
    answer.pop()
    back(depth+1,P-p[depth],F-f[depth],S-s[depth],V-v[depth],C-c[depth],answer)

back(0,0,0,0,0,0,[])

if min != 100000:
    print(min)
    print(*result)
else:
    print(-1)
