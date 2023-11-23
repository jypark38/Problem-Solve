
function checkL(target,key){
    if(key[0].includes(target)){
        return true
    }
    return false
}

function checkR(target,key){
    if(key[2].includes(target)){
       return true
    }
    return false
}

function solution(numbers, hand) {
    var answer = '';
    var left=[0,3],right=[2,3]
    var _hand = hand==='right' ? 'R' : 'L'
    var l = [1,4,7]
    var r = [3,6,9]
    var c = [2,5,8,0]
    
    var key = [[1,4,7,'*'],
               [2,5,8,0],
               [3,6,9,'#']]
    
    for(i=0;i<numbers.length;i++){
        target = numbers[i]
        if(checkL(target,key)){
            left = [0,key[0].indexOf(target)]
            answer += 'L'
            continue
        }
        if(checkR(target,key)){
            right = [2,key[2].indexOf(target)]
            answer += 'R'
            continue
        }
        targetIdx = [1,key[1].indexOf(target)]
        distanceL = Math.abs(left[0] - 1) + Math.abs(left[1] - targetIdx[1])
        distanceR = Math.abs(right[0] - 1) + Math.abs(right[1] - targetIdx[1])
        
        if(distanceL === distanceR){
            answer+=_hand
            if(_hand === 'L'){
                left = targetIdx
            } else{
                right = targetIdx
            }
        } else if (distanceL > distanceR){
            answer += 'R'
            right = targetIdx
        } else {
            answer += 'L'
            left = targetIdx
        }
    }
    return answer;
}


