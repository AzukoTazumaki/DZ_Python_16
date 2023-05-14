

window.onload = function () {
    document.body.classList.add('loaded_hiding');
    window.setTimeout(function () {
        document.body.classList.add('loaded');
        document.body.classList.remove('loaded_hiding');
    }, 500);
}

/*————————————————————————————————————WEB—SOCKET————————————————————————————————————*/

let socket = io()

/* GREATEST COMMON DIVISOR */
const gcd_button = document.getElementById('gcd_submit')
const gcd_form = document.getElementById('gcd_form')
const gcd_result = document.getElementById('ex_1_result')

gcd_button.onsubmit = event => {
    event.preventDefault()
    
}

