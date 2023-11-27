n = int(input())

star = lambda i : (n-abs(n-(i+1)))
space = lambda i : abs(n-(i+1))

result = [' '*space(i)+'*'*star(i) for i in range(2*n-1)]
print('\n'.join(result))