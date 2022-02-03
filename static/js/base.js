$(document).ready(function () {
    if (document.title == 'DENOV') {
        document.querySelector('.header').classList.add('ontop');
    }
});


var prevScrollpos = window.pageYOffset;
window.onscroll = function () {
    var currentScrollPos = window.pageYOffset;
    if (prevScrollpos > currentScrollPos) {
        document.getElementById("header").style.top = "0";
    } else {
        document.getElementById("header").style.top = "-112px";
        document.querySelector(".dropdown-menu").classList.remove('show');

    }
    prevScrollpos = currentScrollPos;

    if (document.title == 'DENOV') {
        var scrolled = window.pageYOffset || document.documentElement.scrollTop; // Получаем положение скролла
        if (scrolled !== 0) {
            // Если прокрутка есть, то делаем блок прозрачным
            document.querySelector('.header').classList.remove('ontop');
        } else {
            // Если нет, то делаем его полностью видимым
            document.querySelector('.header').classList.add('ontop');
        }
        ;
    }
    document.querySelector(".collapse").classList.remove('show');
};


function myFunction() {
    console.log("asdasdasd")
    ;
}