const listItems =  document .querySelectorAll(".sidebar li ul");
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