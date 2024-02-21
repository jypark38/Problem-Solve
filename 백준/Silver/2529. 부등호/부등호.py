import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

k = int(input())
oper = input().split()

MAX = 0
MIN = 10**(k+1)

def backtrack(depth,node,string):
    global MAX,MIN
    if depth==k:
        # print(string)
        result = int(string)
        if result > int(MAX):
            MAX = string
        if result < int(MIN):
            MIN = string
        return

    if oper[depth] == '<':
        for i in range(node+1,10):
            if str(i) in string:
                continue
            backtrack(depth+1,i,string+str(i))
    
    elif oper[depth] == '>':
        for i in range(0,node):
            if str(i) in string:
                continue
            backtrack(depth+1,i,string+str(i))

for i in range(0,10):
    backtrack(0,i,str(i))

print(MAX)
print(MIN)