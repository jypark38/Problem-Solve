import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

def rebuild_tree(post_start, post_end, in_start, in_end):
    if post_start > post_end or in_start > in_end:
        return
    
    root = postorder[post_end]
    print(root,end=' ')
    root_idx = idx[root]

    left_size = root_idx - in_start

    rebuild_tree(post_start, post_start + left_size -1, in_start, root_idx - 1)
    rebuild_tree(post_start + left_size, post_end-1, root_idx+1, in_end)


n = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int,input().split()))

idx = {inorder[i]: i for i in range(n)}
rebuild_tree(0,n-1,0,n-1)

