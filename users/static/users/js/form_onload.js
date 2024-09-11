function changeContentDivHeight() {
    document.getElementsByClassName("content")[0].setAttribute('style', `height:${screen.height-document.getElementsByClassName("navbar")[0].clientHeight}px`)
}

changeContentDivHeight()

window.addEventListener("orientationchange", (e) => {
    changeContentDivHeight()
})

if (window.location.href.includes("register")) {
    document.querySelector(".register-button").classList.add("selected")
} else {
    document.querySelector(".login-button").classList.add("selected") 
}