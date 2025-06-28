async function consultaMarvelAPI() {
  const url = 'https://gateway.marvel.com/v1/public/characters?apikey=74b43c84091b507498b9e6cbb7fc900f&ts=1741753052&hash=0b6fea8c4698e109b66b4aca3f5488ac';

  console.time('Consulta Marvel');
  try {
    const response = await fetch(url);
    const data = await response.json();
    console.timeEnd('Consulta Marvel');
    data.data.results.forEach((personaje, index) =>
      console.log(`${index + 1}. ${personaje.name}`)
    );
  } catch (error) {
    console.timeEnd('Consulta Marvel');
    console.error('Error:', error.message);
  }
}

consultaMarvelAPI();