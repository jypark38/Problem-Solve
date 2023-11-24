function solution(food) {
    var answer = '';
    let str = ''
    for(let i=1;i<food.length;i++){
        str += (i+'').repeat(parseInt(food[i]/2))
    }
    answer = str + '0' + Array(...str).reverse().join('')
    
    return answer;
}