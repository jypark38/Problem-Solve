function solution(arr) {
    const m = arr.length
    for(i=0;i<m;i++){
        for(j=0;j<m;j++){
            if(arr[i][j] !== arr[j][i]) return 0
        }
    }
    return 1;
}