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