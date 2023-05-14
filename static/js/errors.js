/*————————————————————————————————————ANIMATIONS————————————————————————————————————*/

const errors_body = document.querySelector('.errors_body');

window.addEventListener('mousemove', function (e) {
    let x = e.clientX / window.innerWidth;
    let y = e.clientY / window.innerHeight;
    errors_body.style.transform = 'translate(-' + x * 40 + 'px, -' + y * 40 + 'px)';
});

const logo_404 = document.querySelector('.logo_404');

window.addEventListener('mousemove', function (e) {
    let x = e.clientX / window.innerWidth;
    let y = e.clientY / window.innerHeight;
    logo_404.style.transform = 'translate(' + x * 40 + 'px, ' + y * 40 + 'px)';
});