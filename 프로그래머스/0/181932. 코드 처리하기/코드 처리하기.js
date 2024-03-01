function solution(code) {
    var ret = '';
    let mode = 0
    
    for(let i=0;i<code.length;i++){
        const c = code[i]
        if(c=='1'){
            mode = !mode*1
            continue
        }
        if(mode==0 && i%2==0){
            ret += c
        }else if(mode==1 && i%2!=0){
            ret += c
        }
    }
    if (ret.length==0) return 'EMPTY'
    return ret;
}