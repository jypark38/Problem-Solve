function solution(arr) {
    var answer = 0;
    const l = arr.length
    while(true){
        newArr = [...arr]
        for(let i=0;i<l;i++){
            if(newArr[i]>=50 && newArr[i]%2==0){
                newArr[i] /= 2
            } else if(newArr[i]<50 && newArr[i]%2==1){
                newArr[i] = newArr[i]*2+1
            }
        }
        let flag = 1
        for(let i=0;i<l;i++){
            if(newArr[i] != arr[i]){
                flag=0
                break
            }
        }
        if(flag==1) break
        answer+=1
        arr=[...newArr]
    }
    return answer;
}