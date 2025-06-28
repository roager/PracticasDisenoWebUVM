let pantalla = document.getElementById("pantalla");

function clika(valor) {
    pantalla.value += valor;
}

function borra() {
    pantalla.value = "";
}

function calcula() {
    try {
        pantalla.value = eval(pantalla.value);
    } catch (error) {
        pantalla.value = "Error";
    }
}