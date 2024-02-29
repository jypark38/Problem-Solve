function solution(str_list, ex) {
    var answer = '';
    for(c of str_list){
        if(c.includes(ex)) continue
        answer+=c
    }
    return answer;
}