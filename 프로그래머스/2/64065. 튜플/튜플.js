function solution(s) {
    var answer = [];
    _s = s.slice(2,-2).split('},{').sort((a,b)=>a.length-b.length)
    _s.forEach((item)=>{
        arr = item.split(',')
        arr.forEach(e=>answer.push(e*1))
    })
    
    
    answer = Array.from(new Set(answer))
    
//     let _s = s.replaceAll('{','')
//     _s = _s.replaceAll('}','')
//     const arr = _s.split(',')
//     const setArr = Array.from(new Set(arr))
//     const objArr = []
//     console.log(setArr)
//     setArr.forEach((e)=>{
//       objArr.push({
//           value:e,
//           cnt:0
//       })  
//     })
    
//     for(i=0;i<arr.length;i++){
//         for(j=0;j<setArr.length;j++){
//             if(arr[i] === objArr[j].value){
//                 objArr[j].cnt += 1
//             }
//         }
//     }
    
//     objArr.sort((a,b)=>b.cnt-a.cnt).forEach((e)=>{
//         answer.push(Number(e.value))
//     })
    
    return answer;
}

// 일차원 배열로 만들기
// 원소 수로 내림차순 정렬