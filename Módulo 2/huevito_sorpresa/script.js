let colores = ["pink", "skyblue", "lightgreen", "orange", "lightyellow"];

$("#btnAlerta").click(function(){
    alert("Se hizo click en el botón");
});

$("#btnColor").click(function(){
    //Librería: Math
    //Numero aleatorio entre 0 y 4
    let indice = Math.floor(Math.random() * colores.length);
    /*
    let huevito = document.querySelector("#huevito");
    huevito.style.backgroundColor = "pink";
    */

    $("#huevito").css("background-color", colores[indice]);
    $("#mensaje").text(`¡El huevito cambió al color ${colores[indice]}!`);
});

$("#btnSaltar").click(function(){
    $("#huevito").animate({top: '-=40px'}, 200);
    $("#huevito").animate({top: '+=40px'}, 200);
    $("#mensaje").text("¡Salta salta huevito!");
});

$("#btnAbrir").click(function(){
    /*
    let inputTexto = document.querySelector(".inputTexto");
    inputTexto.value <-VALOR que el usuario escribio en el input
    */

    let valor = $(".inputTexto").val();

    $("#mensaje").text(`Tu sorpresa es: ${valor}`);
});

$(".inputTexto").change(function(){
    console.log("Hubo un cambio en el input");
});

//.fadeOut() .fadeIn()