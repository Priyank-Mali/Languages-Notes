
function isPrime(number){
        for (let start=2;start<=Math.sqrt(number);start++){
                if (number%start == 0){
                        return false
                } 
                
        }
        return true
}

console.log([54,3,4,5,7,11,19,6,7,,4].filter(isPrime)) 