function solution(num_list) {
    let e=0,o=0;
    for(let i=0;i<num_list.length;i++){
        if((i+1)%2 == 0){
            o+=num_list[i]
        }else{
            e+=num_list[i]
        }
    }
    return Math.max(e,o);
}