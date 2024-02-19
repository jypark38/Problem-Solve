n,m = map(int,input().split())

arr = []

def f():
    if len(arr) == m:
        print(*arr)
        return
    else:
        for i in range(n):
            if i+1 in arr:
                continue
            arr.append(i+1)
            f()
            arr.pop()

f()