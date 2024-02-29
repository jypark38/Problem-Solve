function solution(number) {
    const a = number.split('').map(Number).reduce((a,b)=>a+b)
    return a%9;
}