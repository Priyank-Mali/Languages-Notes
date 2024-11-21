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
        sidebar.className = "fa-solid fa-xmark";
    } else {
        document.getElementById("sidebar").style.display = "none";
        sidebar.className = "fa-solid fa-bars";

    }
})


// ============================================================================================
// animation

let animation = Array.from(document.getElementsByClassName("animation"))
console.log(animation)