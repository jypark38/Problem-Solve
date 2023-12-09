function solution(my_string) {
    var answer = '';
    for(i of my_string){
        answer = i+answer
    }
    return answer;
}