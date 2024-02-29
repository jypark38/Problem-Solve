function solution(my_string) {
    var answer = Array(52).fill(0);
    for(c of my_string){
        const code = c.charCodeAt()
        if(97<=code && code<=122){
            answer[code-71]++
        }
        if(65<=code && code<=90){
            answer[code-65]++
        }
    }
    return answer;
}

/*
97
122
65
90
*/