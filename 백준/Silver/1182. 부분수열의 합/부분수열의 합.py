import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n,s = map(int,input().split())
nums = list(map(int,input().split()))
cnt = 0
def backtrack(total, idx):
    global cnt
    if idx >= n:
        return

    total += nums[idx]

    if total == s:
        cnt += 1

    backtrack(total,idx+1)
    backtrack(total-nums[idx],idx+1)

backtrack(0,0)

print(cnt)