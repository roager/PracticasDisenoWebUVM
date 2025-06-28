
$(document).ready(function() {
    $("#mudar-cores").click(function() {
        $("#caixinhas").toggleClass("flex-containerb");
        $("#caixinhas > div").toggleClass("flex-containerb");
    });
    $("#arredondar").click(function() {
        $("#caixinhas").toggleClass("flex-container-squared");
        $("#caixinhas > div").toggleClass("flex-container-squared");
    });
    $("#acrescentar-caixa").click(function() {
        let maisUmaCaixinha = $("#caixinhas > div").length + 1;
        $("#caixinhas").append("<div>" + maisUmaCaixinha + "</div>");
    });
});