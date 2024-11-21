// slider
// =======================================================

let currentIndex = 0;
setInterval(()=>{
    let panels = document.querySelectorAll(".panel")
    panels.forEach((e)=>{
        e.classList.remove("active")
    })
    
    panels[currentIndex].classList.add("active")

    currentIndex ++;
    if (currentIndex >= panels.length){
        currentIndex = 0
    }

},2500)


// sidebar
// ==========================================================
let sidebar = document.getElementsByClassName("navbar-responsive")[0].lastElementChild
sidebar.addEventListener("click",()=>{
    if (sidebar.className == "fa-solid fa-bars"){
        document.getElementById("sidebar").style.display = "block";
        document.getElementById("sidebar").children[0].classList.add("slide")
        sidebar.className = "fa-solid fa-xmark";
    } else {
        document.getElementById("sidebar").style.display = "none";
        sidebar.className = "fa-solid fa-bars";
        document.getElementById("sidebar").children[0].classList.remove("slide")

    }
});


// ============================================================================================
// animation

// let animation = Array.from(document.getElementsByClassName("animation"))


// ================================================================================================
// shoppingcart

function shoppingCart(){
    let shoppingcart = document.getElementById("shoppingcarticon")
    let cartsidebar =  document.querySelector(".cartsidebar")
    let closecart = document.querySelector(".closecart")
    cartsidebar.style.display = "block";

    closecart.addEventListener("click",()=>{
        cartsidebar.style.display = "none";
    })
    
    return false
}


// ======================================================================================================
// searchbar

function searchBar(){
    document.querySelector(".searchbar").style.display = "block"
    document.getElementById("closesearchbar").addEventListener("click",()=>{
        document.querySelector(".searchbar").style.display = "none"
    })

    return false
}
