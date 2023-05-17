function solution(n) {
    var answer = 0;
    
    arr = (n+'').split('')
    
    answer = arr.sort().reverse().join('')*1
    
    return answer;
}