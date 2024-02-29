function solution(n, slicer, num_list) {
    var answer = [];
    let s,e,step=1
    if(n==1){
        s=0
        e=slicer[1]+1
    }else if(n==2){
        s=slicer[0]
        e=num_list.length
    }else if(n==3){
        s=slicer[0]
        e=slicer[1]+1
    }else{
        s=slicer[0]
        e=slicer[1]+1
        step=slicer[2]
    }
    for(let i=s;i<e;i+=step){
        answer.push(num_list[i])
    }
    return answer;
}