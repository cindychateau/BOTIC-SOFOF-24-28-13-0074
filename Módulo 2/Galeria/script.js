let images = $(".thumb"); //Lista de todas las imágenes
let currentIndex = 0;

$(".thumb").click(function(){
    let src_imagen = $(this).attr("src");
    $(".image-modal").attr("src", src_imagen);
    $(".modal").fadeIn();

    //let index = $(this).attr("data-index");
    currentIndex = $(this).attr("data-index");
});

$(".close").click(function(){
    $(".modal").fadeOut();
});

$("#prev").click(function(){
    currentIndex = (currentIndex - 1 + images.length) % images.length;
    let src_imagen = $(images[currentIndex]).attr("src");
    $(".image-modal").attr("src", src_imagen);
});

$("#next").click(function(){
    currentIndex = (currentIndex + 1 + images.length) % images.length;
    let src_imagen = $(images[currentIndex]).attr("src");
    $('.image-modal').attr("src", src_imagen);
});