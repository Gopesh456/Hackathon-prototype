const result = document.querySelectorAll(".result")

for (let i = 0;i < 10;i++){
    if(result[i].textContent == 'Correct'){
        console.log(result[i].textContent)
        result[i].style.color = 'Green'
    }else if (result[i].textContent == 'Incorrect'){
        console.log(result[i].textContent)
        result[i].style.color = 'Red'

    }
}
