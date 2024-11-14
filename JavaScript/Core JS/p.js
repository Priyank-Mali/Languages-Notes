const user = {
    name : "priyank",
    price : 999,

    welcomeMsg : function(){
        return `welcome, ${this.name}`
    }
}


console.log(user.welcomeMsg())
