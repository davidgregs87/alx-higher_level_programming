// A jQuery script that fetches the list of titles in a URL and append it to the div tag

$.getJSON('https://swapi-api.alx-tools.com/api/films/?format=json', function (data, textStatus) {
    if(textStatus === 'success') {
        const films = data.results;
        films.forEach(film => {
            $('UL#list_movies').append('<li>' + film.title + '</li>');
        });
    }
})