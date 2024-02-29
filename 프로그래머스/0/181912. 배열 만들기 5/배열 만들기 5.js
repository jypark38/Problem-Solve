function solution(intStrs, k, s, l) {
    return intStrs.map((e)=>e.slice(s,s+l)*1).filter(e=>e>k)
}