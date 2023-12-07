const listItems = document .querySelectorAll(".sidebar-list li");

listItems.forEach(item =>{
    item.addEventListener("click",()=>{
        let isActive = item.classList.contains("active");

        listItems.forEach(e1 =>{
            e1.classList.remove("active");
        })

        if (isActive) item.classList.remove("active");
        else item.classList.add("active");
    });
});
const menuBar = document.querySelector('.content nav .bx.bx-menu');
const sideBar = document.querySelector('.sidebar');

menuBar.addEventListener('click', () => {
    sideBar.classList.toggle('close');
});

window.addEventListener('resize', () => {
    if (window.innerWidth < 768) {
        sideBar.classList.add('close');
    } else {
        sideBar.classList.remove('close');
    }
    if (window.innerWidth > 576) {
        searchBtnIcon.classList.replace('bx-x', 'bx-search');
        searchForm.classList.remove('show');
    }
});
const toggler = document.getElementById('theme-toggle');

toggler.addEventListener('change', function () {
    if (this.checked) {
        document.body.classList.add('dark');
    } else {
        document.body.classList.remove('dark');
    }
});