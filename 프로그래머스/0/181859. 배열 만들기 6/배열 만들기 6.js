function solution(arr) {
    var stk = [];
    let i =0;
    while(i<arr.length){
        if(stk.length==0){
            stk.push(arr[i])
        }else{
            const l = stk.length
            if(stk[l-1] == arr[i]){
                stk.pop()
            }else{
                stk.push(arr[i])
            }
        }
        i+=1
    }
    return stk.length ? stk : [-1];
}