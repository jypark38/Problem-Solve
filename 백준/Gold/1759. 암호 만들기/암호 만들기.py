import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

l,c = map(int,input().split())
arr = input().split()
arr.sort()
def back(depth,str):
    if len(str) == l:
        cnt = 0
        cnt2 = 0
        for char in str:
            if char in 'aeiou':
                cnt+=1
            else:
                cnt2+=1
        if cnt>=1 and cnt2>=2:
            print(str)
        return
    
    for i in range(c):
        if arr[i] in str or (len(str) and str[-1] >= arr[i]):
            continue
        back(depth+1,str+arr[i])

back(0,'')