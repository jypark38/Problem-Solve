def solution(A, B):
    answer = 0
    _A = A
    while answer<len(B):
        if(B==_A): break
        answer += 1
        _A = _A[-1] + _A[:-1]
        print(_A)
        
    if answer==len(B): answer=-1
        
    return answer