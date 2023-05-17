function solution(num) {
    var answer = 0;
    let cnt = 0;
    while(num!==1 && cnt<500){
        if(num%2){
           num = num*3+1 
        } else{
            num /= 2
        }
        cnt++;
    }
    if(cnt>=500){
        cnt = -1
    }
    
    return cnt;
}