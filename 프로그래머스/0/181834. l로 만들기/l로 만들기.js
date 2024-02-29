function solution(myString) {
    var answer = '';
    for(c of myString){
        if (c < 'l') answer+='l'
        else answer+=c
    }
    return answer;
}