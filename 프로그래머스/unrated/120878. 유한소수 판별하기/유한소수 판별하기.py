import math

def solution(a, b):
    answer = 0
    
    g = math.gcd(a,b)
    if g>1: 
        a//=g
        b//=g
        
        
    dv = 2
    _b = b
    while _b!=1:
        if not _b % dv:
            if not (dv == 2 or dv == 5):
                return 2
            _b/=dv
            dv=2
            continue
        dv+=1
        
    return 1