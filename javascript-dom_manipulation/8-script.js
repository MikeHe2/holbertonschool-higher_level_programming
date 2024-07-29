const url = "https://hellosalut.stefanbohacek.dev/?lang=fr";
fetch(url)
  .then((response) => response.json())

  .then((data) => {
    document.getElementById('hello').textContent = data['hello']
    });