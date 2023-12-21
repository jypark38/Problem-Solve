def sum(n,p):
    result = 0
    t=n
    while t>0:
        result += (t%10)**p
        t//=10
    return result

a,p = map(int,input().split())

visited= [0 for _ in range((9**5)*4+1)]

cnt = 1
visited[a] = cnt
while 1:
    next = sum(a,p)
    if visited[next]:
        break
    a = next
    cnt+=1
    visited[a] = cnt

print(visited[next]-1)