function solution(binomial) {
    var answer = 0;
    let [a,o,b] = binomial.split(' ')
    a *= 1
    b *= 1
    if(o=='+'){
        return a+b
    } else if(o=='-'){
        return a-b
    } else{
        return a*b
    }
}