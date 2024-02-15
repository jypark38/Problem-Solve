import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

arr = []
while True:
    try:
        arr.append(int(input()))
    except:
        break

def post(tree,start_idx, end_idx):
    if start_idx > end_idx:
        return
    
    root = tree[start_idx]
    right = end_idx+1

    for i in range(start_idx, end_idx+1):
        if tree[i] > root:
            right = i
            break

    post(tree, start_idx+1, right-1)
    post(tree, right, end_idx)
    print(root)

post(arr,0,len(arr)-1)