// The filter() method of Array instances creates a shallow copy of a portion of a given array
// filter() ===============================================================

const arr = [1,2,3,4,5,6,7,8,9,10]

const new_arr = arr.filter((num)=>num>5)
console.log(new_arr)


// map() ===============================================================

const arr1 = [2,3,4,5,6,7,8,9]
const new_arr1 = arr1.map((num)=>num*2)
console.log(new_arr1)


// reduce() =============================================================== 
const mynums = [1,2,3]

// const total = mynums.reduce(function(accumulator,currentValue){
//     console.log(`accumulator : ${accumulator} and currentvalue : ${currentValue}`)
//     return accumulator + currentValue
// },0) // initialvalue

const total = mynums.reduce((accumulator,currentValue) => accumulator + currentValue , 0)

console.log(total)


// chaining ===============================================================

const mynumbers = [1,2,3,4,5,6,7,8,9,10]

const new_mynumbers = mynumbers.map((num)=>num*10).map((num)=>num+1).filter((num)=>num>30)
console.log(new_mynumbers)


