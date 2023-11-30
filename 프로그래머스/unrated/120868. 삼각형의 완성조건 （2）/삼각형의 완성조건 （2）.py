def solution(sides):
    b = max(sides)
    s = min(sides)
    answer = []
    for i in range(1,3001):
        if(b+s>i and b<=i):
            answer.append(i)
        elif(s+i>b and b>=i):
            answer.append(i)
    
    return len(answer)

print(solution([3,3]))