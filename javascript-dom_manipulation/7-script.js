const url = "https://swapi-api.hbtn.io/api/films/?format=json";
fetch(url)
  .then((response) => response.json())

  .then((data) => {
    info = data['results']
    const li = document.getElementById('list_movies');

    for (episodes in info) {
        const item = document.createElement('li');
        item.textContent = info[episodes]['title'];
        li.appendChild(item);
    }
  });