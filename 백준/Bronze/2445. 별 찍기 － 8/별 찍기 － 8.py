n = int(input())

result = ['*'*(n-abs(n-(i+1)))+' '*abs(2*(n-(i+1)))+'*'*(n-abs(n-(i+1))) for i in range(2*n)]
print('\n'.join(result))