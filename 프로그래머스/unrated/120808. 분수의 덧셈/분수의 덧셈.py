import math

def solution(numer1, denom1, numer2, denom2):
    answer = []
    denom = denom1 * denom2
    numer = numer1*denom2 + numer2*denom1
    g = math.gcd(denom,numer)
    
    return [numer//g,denom//g]