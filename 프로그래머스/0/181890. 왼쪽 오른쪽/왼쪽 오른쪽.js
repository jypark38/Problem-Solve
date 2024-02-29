function solution(str_list) {
    var answer = [];
    let l,r
    for(let i=0;i<str_list.length;i++){
        if(str_list[i]=='l'){
            l=i
            break
        }
        if(str_list[i]=='r'){
            r=i
            break
        }
    }
    if(l!=undefined){
        return str_list.slice(0,l)
    }
    if(r!=undefined){
        return str_list.slice(r+1,str_list.length)
    }
    return [];
}

console.log(solution(['r','b','b','b']))
// console.log(solution(['a','a','l']))
// console.log(solution(['a','a','b','b','b']))