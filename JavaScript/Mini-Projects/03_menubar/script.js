// let showMenu = (cls) =>{
//     let nav = document.getElementById("nav");
//     nav.classList.toggle("nav-show");
// }

let slideshow = (cls) =>{
    let nav = document.getElementById("navslide");
    let icon1 = document.getElementById("icon1");
    if(icon1.classList.contains("fa-bars")){
        icon1.classList.remove("fa-bars")
        icon1.classList.add("fa-xmark")
    }else{
        icon1.classList.add("fa-bars")
        icon1.classList.remove("fa-xmark")
    }
    nav.classList.toggle("slideshow");
}