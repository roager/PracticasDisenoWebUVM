import axios from 'axios';

async function consultaLenta() {
  console.time('Tiempo de espera API lenta');
  const respuesta = await axios.get('https://httpbin.org/delay/6');
  console.timeEnd('Tiempo de espera API lenta');
  console.log('Respuesta recibida');
}

consultaLenta();
