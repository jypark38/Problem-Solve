function solution(myString) {
    var answer = [];
    return myString.split('x').map(e=>e.length);
}