n = int(input())
result = [' '*i+'*'*(n-i) for i in range(n)]
print('\n'.join(result))