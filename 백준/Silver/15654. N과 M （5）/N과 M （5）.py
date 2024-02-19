import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n, m = map(int,input().split())
arr = list(map(int,input().split()))
answer = []
arr.sort()

def backtrack():
    if len(answer) == m:
        print(*answer)
        return

    for i in range(n):
        if arr[i] in answer:
            continue
        answer.append(arr[i])
        backtrack()
        answer.pop()

backtrack()