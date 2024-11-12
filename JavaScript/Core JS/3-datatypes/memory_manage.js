
// Primitive : string / number / boolean / null / undefined / symbol / bigint

// Non-Premitive (reference) : Array / Object / Function

// ==================================================================

// Stack (Primitive) ,  Heap (Non-Premitive)

let name1 = "priyank"

let name2 = name1

console.log(name2)

name2 = "rahul"

console.log(name1) // not changed bcoz it gives copy to anothger name
console.log(name2)

// ===================================================================

let userOne = {
    email : "priyank@gmail.com"
}

let userTwo = userOne // not copying // assigning by reference

userTwo.email = "rahul@gmail.com"

console.log(userOne) // both are at same reference
console.log(userTwo)