def solution(s):
    
    string = ''
    
    for c in s:
        if s.count(c) == 1:
            string+=c
    return ''.join(sorted(string))