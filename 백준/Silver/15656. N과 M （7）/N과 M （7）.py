import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n, m = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()

result = []

def back(depth):

    if depth == m:
        print(*result)
        return
    
    for i in range(n):
        result.append(arr[i])
        back(depth+1)
        result.pop()

back(0)
