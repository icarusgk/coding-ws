import fetch from 'node-fetch';

const tmdbKey = '40f6a5ca2cd6007653138bc57815a86f';
const tmdbBaseUrl = 'https://api.themoviedb.org/3';

const getGenres = async () => {
  const genreEndpoint = '/genre/movie/list';
  const requestParams = `?api_key=${tmdbKey}`;

  const urlToFetch = `${tmdbBaseUrl}${genreEndpoint}${requestParams}`;

  try {
    const response = await fetch(urlToFetch);
    if (response.ok) {
      const jsonResponse = await response.json();
      const { genres } = jsonResponse;
      return genres;
    }
  } catch (err) {
    console.log(err);
  }
}

console.log(await getGenres());