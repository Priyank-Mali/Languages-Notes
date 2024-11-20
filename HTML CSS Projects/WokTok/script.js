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
