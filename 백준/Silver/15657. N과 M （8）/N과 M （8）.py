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
        if (len(answer) and arr[i] < answer[-1]):
            continue
        answer.append(arr[i])
        backtrack()
        answer.pop()

backtrack()