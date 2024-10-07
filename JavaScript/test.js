let obj = {
    name : "psiyan",
    jasd : "adkjasd",
    asdhk : "adlsad"
}

// for (const key in obj) {
//     if (Object.prototype.hasOwnProperty.call(obj, key)) {
//         console.log(`${key} --> ${obj[key]}`);  
//         console.log(`${key} --> ${obj.key}`);  
//     }
// }

arr = [11,12,13,14]

arr.forEach((index,value) => {
    console.log(value,index);
});

// console.log(Object.keys(obj))

// Object.keys(obj).forEach(element => {
//     console.log(obj[element]);
// })