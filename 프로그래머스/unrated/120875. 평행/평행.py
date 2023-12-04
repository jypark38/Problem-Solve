from itertools import combinations

def solution(dots):
    answer = 0
    
    comb = list(combinations([0,1,2,3],2))
    
    for i in range(0,3):
        l1 = list(comb[i])
        l2 = list(comb[5-i])
        d01 = dots[l1[0]]
        d02 = dots[l1[1]]
        d11 = dots[l2[0]]
        d12 = dots[l2[1]]
        
        m1 = (d01[1] - d02[1]) / (d01[0] - d02[0])
        m2 = (d11[1] - d12[1]) / (d11[0] - d12[0])
        if(m1==m2) : 
            return 1
    
    return answer