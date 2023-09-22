function login(element) {
    if(element.innerText=="Login") {
        element.innerText=
        "Logout";
    } else {
        element.innerText="Login"
    }
}

function hide(element) {
    element.remove();
}

let count = 0
function message() {
    count += 2 
    document.getElementById("count").innerText = count
    alert(count);
}

let numbers = 0
function Cookies() {
    numbers -= 1
    document.getElementById("numbers").innerText = numbers 
}

