function solution(num_list) {
    var answer = 0;
    for(n of num_list){
        let k = n
        while(k!=1){
            if(k%2){
                k = (k-1)/2
            }else{
                k/=2
            }
            answer+=1
        }
    }
    return answer;
}