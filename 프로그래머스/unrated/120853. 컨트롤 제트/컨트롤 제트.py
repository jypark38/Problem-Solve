def solution(s):
    answer = []
    _s = s.split()
    
    for c in _s:
        if c == 'Z':
            answer.pop()
        else:
            answer.append(int(c))
    
    return sum(answer)