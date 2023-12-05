from collections import deque
import sys

input = sys.stdin.readline

N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
M = int(input())
C = list(map(int,input().split()))
data = deque([B[i] for i in range(N) if A[i] == 0])
N = len(data)
answer = []
for c in C:
    data.appendleft(c)
    answer.append(data.pop())
print(*answer)