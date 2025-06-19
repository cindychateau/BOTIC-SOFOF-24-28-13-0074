console.log("¡Hola desde Javascript!");

function muestraAlerta() {
    alert("Hiciste click al botón");
}

let botonEstilos = document.querySelector("#btnEstilos");
let mensaje = document.querySelector(".mensaje");

botonEstilos.addEventListener("click", function(){
    mensaje.style.fontSize = "40px";
    mensaje.style.color = "green";
    mensaje.style.backgroundColor = "lightgreen";
});

let botonOcultar = document.querySelector("#btnOcultar");
botonOcultar.addEventListener("click", function(){
    mensaje.style.display = "none";
});

let mostrar = document.querySelector("#btnMostrar");
mostrar.addEventListener("click", function(){
    mensaje.style.display = "block";
});

let elementoImagen = document.querySelector("#imagen");
elementoImagen.addEventListener("mouseover", function(){
    this.src = "img/otro_gatito.png";
});

elementoImagen.addEventListener("mouseout", function(){
    this.src = "img/gatito.jpg";
});

let botonCambiarTxt = document.querySelector("#btnCambiarTexto");
botonCambiarTxt.addEventListener("click", function(){
    //mensaje.textContent = "Mensaje cambiado magicamente";
    //.querySelector("#entradaTexto");
    let inputTexto = document.querySelector("input[type='text']");
    let inputPorId = document.getElementById("entradaTexto");

    mensaje.textContent = inputTexto.value;
});

let botonEliminar = document.querySelector("#btnEliminar");
botonEliminar.addEventListener("click", function() {
    this.remove(); //.remove() eliminamos el elemento
});

let botonAgregarClase = document.querySelector("#btnClases");
botonAgregarClase.addEventListener("click", function(){
    /*
    mensaje.classList = [
        "mensaje",
        "otraClase"
    ]
    
    */
    mensaje.classList.toggle("resaltado");
});