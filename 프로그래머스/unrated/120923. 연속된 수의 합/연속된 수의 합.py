def solution(num, total):
    answer = []
    
    c = total//num
    s = 0
    
    for i in range(c-num-1,c+num+2):
        print(i)
        if(total == num*(2*i+num-1)//2):
            s = i
            break
            
    for i in range(num):
        answer.append(s)
        s+=1
    
    return answer