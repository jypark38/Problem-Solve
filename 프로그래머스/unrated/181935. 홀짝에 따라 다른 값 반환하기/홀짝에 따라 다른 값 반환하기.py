def solution(n):
    answer = 0
    start = 1 if n%2 else 2
    for i in range(start,n+1,2):
        if start==1:
            answer += i
        else:
            answer += i**2
    return answer