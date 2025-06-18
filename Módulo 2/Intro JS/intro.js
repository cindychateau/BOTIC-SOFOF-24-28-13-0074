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

/*
i = 0
¡Hola!
¿Cómo estás?
---
i = 1
¡Hola!
¿Cómo estás?
---
i = 2
¡Hola!
¿Cómo estás?
---
i = 3
¡Hola!
¿Cómo estás?
---
i = 4
Termina el ciclo
*/
for(let i=0; i < 4; i++) { // i+= 1 o i++
    console.log("¡Hola!");
    console.log("¿Cómo estás?");
}

for(let i=10; i > 0; i--) { //for(inicialización; condicional; paso)
    console.log(i);
}

/*
x = 0
Entramos al while
x = 1;
--
Entramos al while
x = 2;
--
Entramos al while
x = 3
*/
let x = 0;
while(x < 3) {
    console.log("Entramos al while");
    x++; //Aumentamos en 1 la x
}
/*
inicio = 2
final = 12
Entramos al 2do While
inicio = 4
final = 11
--
Entramos al 2do While
inicio = 6
final = 10
--
Entramos al 2do While
inicio = 8
final = 9
--
Entramos al 2do While
inicio = 10
final = 8
*/
let inicio = 2;
let final = 12;
while(inicio < final) {
    console.log("Entramos al 2do While");
    inicio += 2;
    final--;
}

// ARRAY/ARREGLOS/LISTAS
let hobbies = [ "Leer", "Correr", "Bailar", "Cantar", "Jugar videojuegos", "Tocar la guitarra" ];

console.log(hobbies[2]);

hobbies[1] = "Nadar";
console.log(hobbies);

console.log(hobbies.length); // 6 = elementos en el array

//A través de un bucle puedo recorrer un array
for(let z=0; z < hobbies.length; z++) {
    console.log(hobbies[z]);
} 

let combinado = [
    1.11, //0
    "texto", //1
    true, //2
    30, //3
    [1, 2, 3] //4
];

let nombres = ["Elena", "Juana", "Pedro"];
nombres.push("Pablo");
console.log(nombres);
nombres.pop();
console.log(nombres);

let matriz = [
    [1, 2, 3, 4, 5], //matriz[0]
    [6, 7, 8, 9] //matriz[1]
];

matriz[1].push(10);

let lista_vacia = [];

let estudiante = {
    "id": 1234,
    "nombre": "Elena",
    "apellido": "De Troya",
    "edad": 25,
    "casado": false,
    "cursos": ["Front-End", "Python"],
    "direcciones": [
        {
            "calle": "Av. Sol",
            "num": 123,
            "ciudad": "Lima",
            "pais": "Peru"
        },
        {
            "calle": "Primera Avenida",
            "num": 345,
            "ciudad": "Monterrey",
            "pais": "Mexico"
        }
    ]
};
console.log(estudiante["nombre"]);
console.log(estudiante.apellido);
estudiante["escuela"] = "Skillnest"; //Agregar una clave y valor
console.log(estudiante);

let lista_estudiantes = [
    {
        "id": 1234,
        "nombre": "Elena",
        "apellido": "De Troya"
    },
    {
        "id": 3456,
        "nombre": "Juana",
        "apellido": "De Arco"
    }
]

for(let i=0; i<lista_estudiantes.length; i++) {
    lista_estudiantes[i]['escuela'] = "Escuela"+(i+1);
}

console.log(lista_estudiantes);

//Crea un programa que en una variable diga el nombre de una persona, y en otra variable la hora del día (mañana, tarde o noche). Imprimir: Buenos días, <nombre>. Buenas tardes, <nombre>. Buenas noches, <nombre>
let nombre_persona = "Elena";
let hora_del_dia = "noche"; //mañana, tarde, noche
//Imprimir: Buenas noches, Elena

//Total de edades. Crea un programa que en base a una lista de personas me imprima el total de las edades
let personas = [
    {nombre: "Elena", edad: 20},
    {nombre: "Juana", edad: 30},
    {nombre: "Pedro", edad: 21},
    {nombre: "Pablo", edad: 19}
]

//Imprimir: sumatoria de edades

//Crea un programa que en base a un listado de estudiantes me imprima quién tiene el mejor promedio de calificaciones
let estudiantes = [
    {nombre: "Elena", calificaciones: [90, 85, 100]},
    {nombre: "Juana", calificaciones: [100, 60, 87]},
    {nombre: "Pedro", calificaciones: [56, 98, 99]},
    {nombre: "Pablo", calificaciones: [100, 75, 75]}
]
//Imprime el nombre de la persona con mejor promedio y cuál es




