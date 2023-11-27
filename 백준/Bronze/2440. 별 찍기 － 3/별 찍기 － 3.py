n = int(input())
result = ['*'*(n-i) for i in range(n)]
print('\n'.join(result))