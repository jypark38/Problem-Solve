import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

k = int(input())
arr = list(map(int,input().split()))
max_s = sum(arr)
cnt = 0
x = [0]*(max_s+1)

def back(depth,weight):
    global cnt
    if weight > max_s:
        return
    if depth == k:
        if 1 <= weight <= max_s and x[weight]==0:
            x[weight]=1
            cnt+=1
        return

    back(depth+1,weight)
    back(depth+1,weight+arr[depth])
    back(depth+1,weight-arr[depth])
back(0,0)
print(max_s-cnt)

