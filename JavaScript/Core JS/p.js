let si = new Promise((resolve,reject)=>{

    let father = true
    if (father){
        resolve("papa ne ha bola")
    } else {
        reject("papa ne IAS dhoon liya hai")
    }
})

si.then((msg)=>{
    console.log(msg)
    console.log("yehh , we married soon")
}).catch(()=>{
    console.log("chalo kota")
})