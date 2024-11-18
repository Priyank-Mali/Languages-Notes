
let a = 0
let b = 1

function fibo(num){

        let arr = [a,b]
        
        for (let i=0;i<num-2;i++){
                let sum = a + b
                arr.push(sum)
                a = b
                b = sum
        }
       
        return arr
}

console.log(fibo(10))

