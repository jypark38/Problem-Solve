function solution(cacheSize, cities) {
    var answer = 0;
    let cache = []
    for(let city of cities){
        city = city.toLowerCase()
        if(cache.includes(city)){
            answer+=1
            cache = cache.filter(c=>c!=city)
        }else{
            answer+=5
        }
        cache.push(city)
        if(cache.length>cacheSize){
            cache.shift()
        }
    }
    
    return answer;
}