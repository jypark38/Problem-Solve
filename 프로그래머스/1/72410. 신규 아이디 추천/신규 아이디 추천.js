function solution(new_id) {
    var answer = '';
    
    let id = new_id.toLowerCase()
    
    let str = ''
    for(c of id){
        if(('a'<=c && c<='z') || ('0'<=c && c<='9') || c == '-' || c=='_' || c=='.'){
            str+=c
        }
    }
    while(str.includes('..')){
        str = str.replaceAll('..','.')
    }
    id = str
    str = ''
    for(let i=0;i<id.length;i++){
        if(i==0 || i==id.length-1){
            if (id[i]=='.') continue
        }
        str+=id[i]
    }
    if(str.length==0) str='a'
    
    if(str.length>=16) str=str.substr(0,15)
    id=str
    str=''
    for(let i=0;i<id.length;i++){
        if(i==0 || i==id.length-1){
            if (id[i]=='.') continue
        }
        str+=id[i]
    }
    
    if(str.length<=2){
        str = str.padEnd(3,str[str.length-1])
    }
    id=str
    
    return id;
}