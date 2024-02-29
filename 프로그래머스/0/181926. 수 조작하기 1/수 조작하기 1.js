function solution(n, control) {
    const answer = [...control].reduce((n,c)=>{
        if(c=='w') n+=1
        else if(c=='s') n-=1
        else if (c=='d') n+=10
        else if (c=='a') n-=10
        return n
    },n)
    return answer;
}