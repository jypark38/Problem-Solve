fixedD = 1
m,d = map(int,input().split())
dayOfMonth = [31,28,31,30,31,30,31,31,30,31,30,31]
arr = ['MON','TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
result = (sum(dayOfMonth[:m-1]) + d - fixedD) % 7

print(arr[result])
