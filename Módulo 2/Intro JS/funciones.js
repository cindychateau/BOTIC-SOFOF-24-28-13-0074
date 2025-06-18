/*
Función: Bloque de código al que nosotros nombramos y al que podemos llamar las veces que necesite
*/
//function nombre_funcion(parametro1, parametro2...) {}
function saludo() {
    console.log("Hola");
    console.log("¿Cómo estás?");
}

saludo(); //Llamar a mi función -> Mi función se ejecuta
saludo();
saludo();
saludo();

function saludo_nombre(nombre) { //nombre = "Juana"
    console.log(`¡Hola ${nombre}!`); //¡Hola Juana!
}

saludo_nombre("Elena");
saludo_nombre("Juana");

function saludo_nombre_apellido(nombre, apellido) {
    console.log(`¡Hola ${nombre} ${apellido}!`);
}

saludo_nombre_apellido("Elena", "De Troya");

function sumatoria(num1, num2) { //num1 = 11; num2 = 20
    if(typeof num1 == "number" && typeof num2 == "number") {
        let suma = num1+num2; //suma = 11 + 20 = 31
        return suma; // <-31
    } else {
        console.log("Deben ser numerales")
    }
}

let resultado = sumatoria(11, 20); //resultado = 31
console.log(`El resultado de la suma es: ${resultado}`);

// Sigma -  Escribe una función que sume todos los valores del 1 al 100 en una variable sum y, al final, regrese como resultado 1 + 2 + 3 + ... + 98 + 99 + 100. Deberíamos obtener 5050 al final. OJO: recibe el parámetro n, haz la sumatoria hasta n. 
function sigma(n) { //10. return 1+2+3+4+5+6+7+8+9+10

}