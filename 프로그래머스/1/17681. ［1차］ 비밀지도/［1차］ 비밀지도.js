function solution(n, arr1, arr2) {
    var answer = [];
    const map1 = []
    const map2 = []
    for(let i=0;i<n;i++){
        map1.push(arr1[i].toString(2).padStart(n,0))
        map2.push(arr2[i].toString(2).padStart(n,0))
    }
    for(let i=0;i<n;i++){
        let str=''
        for(let j=0;j<n;j++){
            if(map1[i][j] == 0 && map2[i][j]==0){
                str+=' '
            }else{
                str+='#'
            }
        }
        answer.push(str)
    }
    
    return answer;
}