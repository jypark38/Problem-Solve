function solution(a, b, c) {
    var answer = 0;
    const set = new Set([a,b,c])
    if(set.size==3){
        return (a+b+c)
    }
    if(set.size==2){
        return (a+b+c)*(a**2+b**2+c**2)
    }
    return (a+b+c)*(a**2+b**2+c**2)*(a**3+b**3+c**3)
}