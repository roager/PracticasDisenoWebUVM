document.addEventListener("DOMContentLoaded", function() {

    const container = document.getElementById("caixinhas");
    const btnmudarcores = document.getElementById("mudar-cores");
    const btnarredondar = document.getElementById("arredondar");
    const btnacrescentarcaixa = document.getElementById("acrescentar-caixa");
  
    btnmudarcores.addEventListener("click", function() {
        container.classList.toggle("flex-containerb"); //cambia el estilo del container
        container.querySelectorAll("div").forEach(div => { //cambia el estilo de cada div
            div.classList.toggle("flex-containerb");
        });
    });
    
    btnarredondar.addEventListener("click", function() {
        container.classList.toggle("flex-container-squared");
        container.querySelectorAll("div").forEach(div => {
            div.classList.toggle("flex-container-squared");
        });
    });
    btnacrescentarcaixa.addEventListener("click", function() {
        let maisUmaCaixinha = container.children.length + 1;
        let novaDiv = document.createElement("div");
        novaDiv.textContent = maisUmaCaixinha;
        container.appendChild(novaDiv);
      });
  });