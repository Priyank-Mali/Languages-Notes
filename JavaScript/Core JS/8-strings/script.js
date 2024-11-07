
// string : sequence of characters  

let myname = "priyank"
let mycity = 'surat'
console.log(myname,mycity)  
console.log(typeof myname)

/**
 * Accessing character based on index
 */
console.log(myname[4])
console.log(mycity[0])

myname[4] = "o" // (not assign)

// sting is immutable // can't change index value
// that's why it is use to stored sensitive things.
// bcoz in most cases pasword is saved in form of string
// thats why it is immutable 

myname = "priyankmali"
console.log(myname.length)

let fname = "abdul"
let lname = "kalam"
// let fullname = fname + " " + lname
let fullname = fname.concat(lname)
console.log(fullname)

// Template Literals (another way to define string)

let sentance = `This is a template literal`;
console.log(sentance)

let number = 19;
console.log(`The Number is : ${number}`)  // this print as part of string 
console.log("The Number is :",number)    // this print heighlighted value

console.log(`${1+2+4+7}`);

console.log("priyank\tmali".length) // count as single character: -> "\t" or "\n" 

/*
string methods: these are built-in function to manipulate a string.
*/

let name = "MAliPriyanK"
console.log(name.toUpperCase())
console.log(name.toLowerCase())
console.log(name) // original string is stay as it -> does not change(immnutable)

name = "    priyank  mali      "
console.log(name.trim())

/*
slicing --> slicing does not change original string
*/
let st = "priyankmali"
console.log(st.slice(2,5)) // same as python

/**
 * indexof
*/
console.log(st.indexOf("k"))

let str = "hello"
console.log(str.replace("h","l"))
// console.log(str); // not changed

str = "helololo"
console.log(str.replace("lo","p"))

console.log(str.replaceAll("lo","p"));

/*
split
*/

str = "priyank rajesh mali"
console.log(str.split());
console.log(str.split(""));
console.log(str.split(" "));


// let str = "priyank";
// let str = new String("priyank");