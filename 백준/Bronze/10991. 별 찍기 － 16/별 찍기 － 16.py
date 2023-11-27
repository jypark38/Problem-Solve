n = int(input())

star = lambda i : i+1
space = lambda i : n -(i+1)

result = [' '*space(i)+'* '*star(i) for i in range(n)]
print('\n'.join(result))