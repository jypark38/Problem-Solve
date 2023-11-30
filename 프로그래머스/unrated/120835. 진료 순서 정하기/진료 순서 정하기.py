def solution(emergency):
    answer = []
    _e = sorted(emergency,reverse=True)
    _d = dict(enumerate(_e))
    _d = dict(zip(_d.values(),_d.keys()))
    for i in emergency:
        answer.append(_d[i]+1)
    
    return answer