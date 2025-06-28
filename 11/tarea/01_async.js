async function obtenerPersonajesMarvel() {
  const url = 'https://gateway.marvel.com/v1/public/characters?apikey=74b43c84091b507498b9e6cbb7fc900f&ts=1741753052&hash=0b6fea8c4698e109b66b4aca3f5488ac';

  console.time('Tiempo de respuesta');
  try {
    const respuesta = await fetch(url);
    const data = await respuesta.json();
    console.timeEnd('Tiempo de respuesta');
    data.data.results.forEach((personaje, index) =>
      console.log(`${index + 1}. ${personaje.name}`)
    );
  } catch (error) {
    console.timeEnd('Tiempo de respuesta');
    console.error('Error al consultar Marvel API:', error.message);
  }
}

obtenerPersonajesMarvel();