def solution(polynomial):
    answer = ''
    x = 0
    r = 0
    for c in polynomial.split(' + '):
        if 'x' in c:
            if c == 'x':
                x+=1
            else:
                x+=int(c[:-1])
        else:
            r += int(c)
    if x>0:
        if x==1: 
            answer += 'x'
        else:
            answer += f'{x}x'
        
        if r>0:
            answer += f' + {r}'
    else:
         answer += f'{r}'   
    
    return answer