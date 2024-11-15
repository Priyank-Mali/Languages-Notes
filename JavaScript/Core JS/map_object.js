// he Map object holds key-value pairs 
// unique values
const map1 = new Map()

map1.set('IN','India')
map1.set('AUS','Austalia')
map1.set('SA','South-Africa')
map1.set('IN','India')

// map1.delete('SA')

console.log(map1)
console.log(map1.size) // 3

for(const [key,value] of map1){
    console.log(key,'->',value)
}