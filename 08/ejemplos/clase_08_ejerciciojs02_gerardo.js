
//1.Declara un array denominado "participantes" con los siguientes nombres: Elena, Carlos, Javier, Laura, Miguel, Patricia (supongamos que estos son los participantes en un concurso y sus posiciones actuales).
let participantes = ["Elena", "Carlos", "Javier", "Laura", "Miguel", "Patricia"];

//2.Muestra la clasificación actual.
function listarParticipantes(participantes) {
    participantes.forEach((participante, i) => {
        console.log(`${i + 1}. ${participante}`);
    });
}
console.log(`Lista Original`);
listarParticipantes(participantes);
//3.A medida que el concurso avanza, se realizan ajustes en las posiciones del array:
//4.Laura supera a Javier.
participantes.splice(2,1)
participantes.splice(3,0,"Javier")
console.log(`Laura supera a Javier.`);
listarParticipantes(participantes);
//5.Patricia es descalificada y se elimina del concurso.
participantes.pop();
console.log(`Patricia es descalificada y se elimina del concurso.`);
listarParticipantes(participantes);
//6.Se incorporan dos nuevos concursantes, Raúl y Sofía, situándose detrás de Elena y antes de Carlos.
participantes.splice(1, 0, "Raúl", "Sofía");
console.log(`Se incorporan dos nuevos concursantes, Raúl y Sofía, situándose detrás de Elena y antes de Carlos.`);
listarParticipantes(participantes);

//7.Una nueva participante, Carmen, toma la posición principal en la clasificación.
participantes.splice(0, 0, "Carmen");
console.log(`Una nueva participante, Carmen, toma la posición principal en la clasificación.`);
//8.Imprime la clasificación actualizada y verifica que se haya realizado correctamente 
listarParticipantes(participantes);

