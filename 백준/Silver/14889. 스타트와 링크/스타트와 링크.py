import sys
input = sys.stdin.readline

n = int(input())
info = []
visited =  [False for _ in range(n)]

for i in range(n):
    info.append(list(map(int,input().split())))

minimum = 1e9

def backtrack(L,idx):
    global minimum
    if L == n//2:
        A = 0
        B = 0
        for i in range(n):
            for j in range(n):
                if visited[i] and visited[j]:
                    A += info[i][j]
                if not visited[i] and not visited[j]:
                    B += info[i][j]

        minimum = min(minimum, abs(A-B))

    else :
        for x in range(idx, n):
            if visited[x] == False:
                visited[x] = True
                backtrack(L+1, x+1)
                visited[x] = False

backtrack(0,0)
print(minimum)