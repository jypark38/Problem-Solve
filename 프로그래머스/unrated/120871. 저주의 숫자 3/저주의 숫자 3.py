def solution(n):
    i = 1
    arr = []
    while(len(arr)!=n):
        if not (i%3 == 0 or '3' in str(i)):
            arr.append(i)
        i+=1
    
    return arr[-1]