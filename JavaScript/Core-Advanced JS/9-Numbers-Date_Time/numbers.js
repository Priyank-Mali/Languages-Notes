// console.log(Number.MAX_VALUE);
// console.log(Number.MIN_VALUE);
// console.log(Number.NEGATIVE_INFINITY);
// console.log(Number.POSITIVE_INFINITY);
// console.log(Number.NaN);
// console.log(Number.EPSILON);


let number = 1;
// console.log(num)

let a = "99";
let num = Number(a);
console.log(num);

let x = Number(true)
console.log(x)

let y = Number("55 66");
console.log(y);

let z = parseInt("23 45");
console.log(z)

let c = Math.round(Math.random()*10)
console.log(c)

console.log(Math.ceil(4.2))
console.log(Math.floor(4.9))

let r = 100
console.log(typeof r.toString())

// random number between 10 - 20

console.log(Math.floor(Math.random()*(20-10+1)) + 10)

/*
    Math.random() generates a random decimal between 0 (inclusive) and 1 (exclusive).
    Math.random() * (20 - 10 + 1) scales it to a range between 0 and 11
    Math.floor(...) rounds down to the nearest whole number, resulting in a number from 0 to 10.
    + 10 shifts this range up to 10-20.
*/