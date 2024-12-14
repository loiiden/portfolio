document.addEventListener("DOMContentLoaded", () => {
    const openBtn = document.getElementById("open-btn");
    const closeBtn = document.getElementById("close-btn");
    const nav = document.querySelector(".side-nav");
    openBtn.addEventListener("click", () =>
    {
            nav.classList.remove("hidden");
    });
    closeBtn.addEventListener("click", () =>
    {
        nav.classList.add("hidden");
    })

});