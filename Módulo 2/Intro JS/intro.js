console.log("¡Hola mundo!"); //Imprime: ¡Hola mundo!
/* Comentario
de
bloque */
let num = 10;
console.log(num); //Imprime: 10
let texto = "Este es un texto";
let decimales = 1.11;
let bool = true; //true o false
num = 11;

const password = "Abc123"; //Variables const NO PUEDEN SER cambiadas
//password = "ABC345"; //Arroja un error TypeError

console.log(num);// Imprime: 11

let despues; //Por defecto tiene valor undefined
console.log(despues); //¿Qué imprime aquí?
despues = "Este texto lo coloqué después";
console.log(despues);
//undefined es DIFERENTE a vacío, null

let num1 = 1;
let num2 = 5;
let suma = num1 + num2; //suma = 1 + 5 = 6

//Concatenar: pegar n textos
let nombre = "Elena de Troya";
let saludo = "¡Hola! Me llamo:";
console.log(saludo+nombre); //Imprime: ¡Hola! Me llamo:Elena de Troya

let otro_nombre = "Juana de Arco";
let edad = 18;
let mensaje = `Mi nombre es ${otro_nombre}, ¿cómo estás? Tengo ${edad} años.`; //Interpolación
let mensaje_concatenado = "Mi nombre es "+otro_nombre+", ¿cómo estás? Tengo "+edad+" años.";
console.log(mensaje);
console.log(mensaje_concatenado);

let combinamos_texto = "ABC";
console.log(combinamos_texto + num1);
console.log(combinamos_texto + num1 + num2);//Comenzamos con texto, el resto de las var considerar como texto
console.log(num1 + num2 + combinamos_texto);
console.log(combinamos_texto + (num1 + num2));

let orden = 10 + 20 / 6; // ¿Cuál es el valor de orden?
//1.- () 2.- /*% 3.- +-

let n = 14;
n += 5; // n = n+5 = 14 + 5 = 19
// += -= /= *= %=

let nombre_completo = "Pedro";
nombre_completo += " Paramo";
console.log(nombre_completo);

//Booleano = true o false
console.log(bool);
console.log(10 > 5);

if(bool) {
    console.log("La variable es verdadera");
} else {
    console.log("la variable es falsa");
}

if(n >= 20) { //19 >= 20
    console.log("N es mayor a 20")
} else {
    console.log("N es menor a 20");
}

//Operadores: > < >= <= == !=

if(n != 10) {
    console.log("N es distinto a 10");
}

//let edad_nino = prompt("Ingresa la edad del niño");
let edad_nino = 3;
if(edad_nino < 2) {
    console.log("Es un bebe");
} else if(edad_nino < 5) {
    console.log("Es un toddler");
} else {
    console.log("Es un infante");
}

let temperatura = 20;
let estaLloviendo = false; //NO esta lloviendo
if(temperatura >= 18 && !estaLloviendo) { // && AND -> Ambas condicionales deben de cumplirse
    console.log("Es un gran día para dar un paseo!");
}else {
    console.log("Otro día daremos un paseo si las condiciones son óptimas");
}

let edad_conductor = 17;
let permisoPadres = true;
if(edad_conductor >= 18 || permisoPadres) { // || OR -> una u otra condicional debe de cumplirse
    console.log("Tienes permiso para obtener tu licencia de conducir.");
}
// ! -> te transforma a lo contrario

let numero_dia = 8;

switch(numero_dia){
    case 1:
    case 8:
        console.log("Lunes");
        break;
    case 2:
        console.log("Martes");
        break;
    case 3:
        console.log("Miércoles");
        break;
    case 4:
        console.log("Jueves");
        break;
    case 5:
        console.log("Viernes... feriado!");
        break;
    case 6:
        console.log("Sabado, a dormir");
        break;
    case 7:
        console.log("Dormingo");
        break;
}