def solution(n):
    arr = [1]
    answer = 0
    
    for i in range(1,12):
        arr.append(i*arr[-1])
        if(arr[-1]>n): 
            answer = i-1
            break
    
    return answer