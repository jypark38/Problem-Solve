function solution(n, k) {
    price = n * 12000 + k * 2000 - parseInt(n/10) * 2000;
    return price;
} 