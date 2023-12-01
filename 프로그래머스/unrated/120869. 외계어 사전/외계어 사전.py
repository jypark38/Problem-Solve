def solution(spell, dic):
    answer = 2
    
    for c in dic:
        _str = c
        if not len(c) == len(spell): continue
        for ch in spell:
            if _str.count(ch) == 1:
                _str = _str.replace(ch,'')
        print(_str)
        if(not len(_str)):
            answer = 1
            break
            
    return answer