function hello(msg){
    console.log(`hi ${msg}`);
}

hello("priyank");


function custom(firstname = "priyank",lastname){
    console.log("Hello "+ firstname + " " + lastname)
}

custom("rahul","mali");