function solution(a, b, c, d) {
    var answer = 0;
    const dic = {}
    for(let n of [a,b,c,d]){
        if(dic[n]==undefined) dic[n]=1
        else dic[n]++
    }
    const entries = Object.entries(dic).map(e=>[e[0]*1,e[1]])
    const l = entries.length
    if(l==1){
        return entries[0][0]*1111
    }
    if(l==2){
        if(entries[0][1] == 2){
            return (entries[0][0]+entries[1][0])*Math.abs(entries[0][0]-entries[1][0])
        }else{
            return entries[0][1]==3 ? (10*entries[0][0]+entries[1][0])**2 : (10*entries[1][0]+entries[0][0])**2
        }
    }
    if(l==3){
        const arr = entries.filter(e=>e[1] !== 2)
        return arr[0][0]*arr[1][0]
    }
    if(l==4){
        return Math.min(...entries.map(e=>e[0]))
    }
    
    return answer;
}