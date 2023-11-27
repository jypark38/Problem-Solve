n = int(input())
result = [' '*(n-i-1)+'*'*(2*(i+1)-1) for i in range(n)]
print('\n'.join(result))