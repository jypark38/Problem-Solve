def solution(babbling):
    answer = 0
    arr = ["aya", "ye", "woo", "ma"]
    
    for c in babbling:
        _c = c
        for u in arr:
            _c = _c.replace(u,'_',1)
        
        if len(_c.replace('_','')) == 0: answer +=1
    
    return answer