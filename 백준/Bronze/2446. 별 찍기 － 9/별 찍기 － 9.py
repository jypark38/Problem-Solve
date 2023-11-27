n = int(input())

star = lambda i : 2*n-2*(n-abs(n-(i+1)))+1
space = lambda i : n - abs(n-(i+1)) - 1

result = [' '*space(i)+'*'*star(i) for i in range(2*n-1)]
print('\n'.join(result))

'''
n = 5
pivot : 5 5 5 5 5 5 5 5 5
i     : 1 2 3 4 5 6 7 8 9
star  : 9 7 5 3 1 3 5 7 9
space : 0 1 2 3 4 3 2 1 0
'''