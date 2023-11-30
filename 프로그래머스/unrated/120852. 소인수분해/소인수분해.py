def solution(n):
    answer =[]
    dv = 2
    while n>1:
        if n%dv == 0:
            answer.append(dv)
            n/=dv
            dv = 2
        else :
            dv += 1
    return sorted(list(set(answer)))