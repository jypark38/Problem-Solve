function solution(myString, pat) {
    for(let i = myString.length;i>=0;i--){
        const temp = myString.slice(0,i)
        if(temp.endsWith(pat)){
            return temp
        }
    }
}