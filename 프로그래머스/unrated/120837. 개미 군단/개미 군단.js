function solution(hp) {
    const first = parseInt(hp / 5); //4.6
    let second = 0; 
    let third = 0;
    console.log(first)

    if ((hp - (first * 5)) > 3) {
        second = 1;
        third = (hp - (first * 5)) - 3;
    } else if ((hp - (first * 5)) === 3) {
        second = 1;
        third = 0;
    } else {
        second = 0;
        third = (hp - (first * 5)) % 3;
    }
    
    console.log(second,third)
    return first + second + third;
}