const url = 'https://gateway.marvel.com/v1/public/characters?apikey=74b43c84091b507498b9e6cbb7fc900f&ts=1741753052&hash=0b6fea8c4698e109b66b4aca3f5488ac';

console.time('Tiempo Marvel API');
fetch(url)
  .then(response => response.json())
  .then(data => {
    console.timeEnd('Tiempo Marvel API');
    data.data.results.forEach((personaje, index) =>
      console.log(`${index + 1}. ${personaje.name}`)
    );
  })
  .catch(error => {
    console.timeEnd('Tiempo Marvel API');
    console.error('Error al obtener datos:', error.message);
  });