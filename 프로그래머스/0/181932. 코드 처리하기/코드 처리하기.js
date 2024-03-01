function solution(code) {
    var ret = '';
    let mode = 0
    
    for(let i=0;i<code.length;i++){
        const c = code[i]
        if(c=='1'){
            mode = !mode*1
            continue
        }
        if(mode==i%2){
            ret += c
        }
    }
    if (ret.length==0) return 'EMPTY'
    return ret;
}