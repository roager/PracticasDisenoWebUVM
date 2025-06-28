import axios from 'axios';

const url = 'https://gateway.marvel.com/v1/public/characters?apikey=74b43c84091b507498b9e6cbb7fc900f&ts=1741753052&hash=0b6fea8c4698e109b66b4aca3f5488ac';

async function consultaConFetch() {
  console.time('Fetch');
  const response = await fetch(url);
  const data = await response.json();
  console.timeEnd('Fetch');
  data.data.results.forEach((personaje, index) =>
    console.log(`[Fetch] ${index + 1}. ${personaje.name}`)
  );
}

async function consultaConAxios() {
  console.time('Axios');
  const { data } = await axios.get(url);
  console.timeEnd('Axios');
  data.data.results.forEach((personaje, index) =>
    console.log(`[Axios] ${index + 1}. ${personaje.name}`)
  );
}

consultaConFetch();
consultaConAxios();