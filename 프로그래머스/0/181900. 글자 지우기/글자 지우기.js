function solution(my_string, indices) {
    return my_string.split('').reduce((a,c,i)=>{
       if(indices.includes(i)) return a
        return a+c
    },'')
}