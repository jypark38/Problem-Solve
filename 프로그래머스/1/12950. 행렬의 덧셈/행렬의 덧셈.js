function solution(arr1, arr2) {
    var answer = [];
    row = arr1.length;
    col = arr1[0].length;
    
    for(let i=0;i<row;i++){
        temp = Array(col).fill(0)
        for(let j=0;j<col;j++){
            temp[j] = arr1[i][j] + arr2[i][j]
        }
        answer.push(temp)
    }
    return answer;
}