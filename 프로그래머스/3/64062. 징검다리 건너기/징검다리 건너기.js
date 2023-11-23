function solution(stones, k) {
    var answer = binarySearch(stones,k,1,200000000);

    return answer;
}

function binarySearch(arr,k,start,end){
    if(start === end){
        return start
    }
    let mid = parseInt((start+end)/2)
    let cnt = 0;
    for(let i=0;i<arr.length;i++){
        if(cnt===k) break
        let value = arr[i] - mid
        value <= 0 ? cnt++ : cnt=0;
    }
    if(cnt===k){
        return binarySearch(arr,k,start,mid)
    }else{
        return binarySearch(arr,k,mid+1,end)
    }   
}